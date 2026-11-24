from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import base64
# from fair_processor import aggregate_scores, generate_radar_chart, upload_to_imagekit
from fair_processor_2 import aggregate_scores_with_manual
from datetime import datetime
from ATHENA_evaluation_metrics import (
    yearOfTrafficMetric,
    anonymityMetric,
    relevanceMetric,
    radarPlot,
    get_citations_from_opencitations
)
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF
import tempfile
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)

# @app.route('/proxy', methods=['POST'])
# def proxy():
#     data = request.get_json()
#     app.logger.info(data.get("tests"))
#     app.logger.info("PROXY")
#     app.logger.info("data:")
#     app.logger.info(data.get("subject"))
    
#     try:
#         test_responses = [
#             requests.post(
#                 f"https://w3id.org/FAIR_Tests/tests/{t}",
#                 json=data,
#                 headers={
#                     "Content-Type": "application/json",
#                     "Accept": "application/json",
#                     "Allow-Control-Allow-Origin": "*",
#                 }
#             ) for t in data.get("tests", [])
#         ]
        
#         # app.logger.info(f"TEST RESPONSES: {test_responses}")

#         # Verificar se a resposta é válida antes de processar
#         response = []
#         for test_response in test_responses:
#             if test_response.status_code == 200:
#                 try:
#                     response.append(test_response.json())
#                 except ValueError:
#                     app.logger.error(f"Erro ao converter resposta para JSON: {test_response.text}")
#             else:
#                 app.logger.error(f"Erro na requisição: {test_response.status_code} - {test_response.text}")
        
#         # app.logger.info(f"JSON RESPONSE: {response}")
#         scores = aggregate_scores_with_manual(
#             response,                         # mesma response do FAIR Metrics
#             levelOfmetadata="3",              # '0'..'4' (string)
#             availability="On request",        # "No" | "On request" | "Yes"
#             format="CSV, RDF"                 # conter "RDF" => dá 1 nos bônus de I1/I2/I3
#         )  # Apenas para log
#         app.logger.info(f"SCORES AGREGADOS: {scores}")

#         return jsonify(response), 200
#     except Exception as e:
#         app.logger.error(f"FALHOU: {e}")
#         return jsonify({"error": "Internal Server Error"}), 500

@app.route('/proxy', methods=['POST'])
def proxy():
    data = request.get_json()
    app.logger.info(data.get("tests"))
    app.logger.info("PROXY")
    app.logger.info("data:")
    app.logger.info(data.get("subject"))

    try:
        # =========================
        # 1) Buscar RDF da URI
        # =========================
        subject_uri = data.get("subject")
        if not subject_uri:
            return jsonify({"error": "Missing 'subject' URI"}), 400

        rdf_resp = requests.get(
            subject_uri,
            headers={"Accept": "text/turtle, application/ld+json;q=0.8, application/rdf+xml;q=0.6"},
            timeout=15
        )
        if rdf_resp.status_code != 200 or not rdf_resp.text:
            app.logger.error(f"Falha ao obter RDF de {subject_uri}: {rdf_resp.status_code}")
            return jsonify({"error": "Failed to fetch RDF from subject"}), 502

        # Parsear o RDF (Turtle)
        g = Graph()
        try:
            g.parse(data=rdf_resp.text, format="turtle")
        except Exception as e:
            app.logger.error(f"Erro ao parsear RDF (turtle): {e}")
            return jsonify({"error": "Invalid RDF Turtle from subject"}), 400

        # =========================
        # 2) Namespaces + localizar Dataset
        # =========================
        DCAT = Namespace("http://www.w3.org/ns/dcat#")
        DCT  = Namespace("http://purl.org/dc/terms/")
        N1   = Namespace("http://purl.org/athena-o#")
        GLOSS= Namespace("https://csrc.nist.gov/glossary/")

        dataset_uri = None
        for s in g.subjects(RDF.type, DCAT.Dataset):
            dataset_uri = s
            break
        if not dataset_uri:
            return jsonify({"error": "Dataset URI not found in fetched RDF"}), 400

        # Helpers de leitura
        def first(g, s, p):
            for o in g.objects(s, p):
                return str(o)
            return None

        def all_values(g, s, p):
            return [str(o) for o in g.objects(s, p)]

        # =========================
        # 3) Extrair LevelOfMetadata (n1:metadata)
        #    texto exemplo: "0 - none - Metadata ..."
        #    pegamos o primeiro dígito 0..4
        # =========================
        import re

        metadata_txt = first(g, dataset_uri, N1.metadata) or ""
        m = re.match(r"\s*([0-4])", metadata_txt)
        levelOfmetadata = m.group(1) if m else "0"  # string '0'..'4'

        # =========================
        # 4) Availability (gloss:termpublicAvailability)
        #    normaliza para "No" | "On request" | "Yes"
        # =========================
        availability_raw = (first(g, dataset_uri, GLOSS.termpublicAvailability) or "").strip()
        # normalizações comuns
        availability_map = {
            "no": "No",
            "yes": "Yes",
            "on request": "On request",
            "onrequest": "On request",
        }
        availability_key = availability_raw.lower().replace("-", " ").strip()
        availability = availability_map.get(availability_key, "No")

       # =========================
        # 5) Format (dct:format) — pode estar no Dataset ou nas Distributions
        #    também checamos dcat:mediaType e mapeamos tipos RDF -> "RDF"
        # =========================
        from rdflib import URIRef, Literal

        def normalize_url(u: str) -> str:
            if not u:
                return ""
            u = u.strip().strip('"').strip("'")
            # se vier sem esquema, adiciona https://
            if not u.lower().startswith(("http://", "https://")):
                # trata casos "www.exemplo.com" ou domínio puro
                if u.startswith("www."):
                    return f"https://{u}"
                return f"https://{u}"
            return u

        def collect_landing_pages(g, dataset_uri, DCAT):
            vals = []
            for o in g.objects(dataset_uri, DCAT.landingPage):
                if isinstance(o, Literal):
                    vals.append(str(o))
                elif isinstance(o, URIRef):
                    vals.append(str(o))
                else:
                    vals.append(str(o))
            # fallback comuns, caso não exista dcat:landingPage
            # (opcional; comente se não quiser heurísticas)
            # FOAF:homepage
            FOAF = Namespace("http://xmlns.com/foaf/0.1/")
            if not vals:
                for o in g.objects(dataset_uri, FOAF.homepage):
                    vals.append(str(o))
            # dcat:accessURL das distributions, como último recurso
            if not vals:
                for dist in g.objects(dataset_uri, DCAT.distribution):
                    for o in g.objects(dist, DCAT.accessURL):
                        vals.append(str(o))
            # normalização + dedup
            seen = set()
            out = []
            for v in vals:
                nv = normalize_url(v)
                if nv and nv not in seen:
                    seen.add(nv)
                    out.append(nv)
            return out

        landing_pages = collect_landing_pages(g, dataset_uri, DCAT)
        landing_page = landing_pages[0] if landing_pages else ""
        app.logger.info(f"[MANUAIS] landingPage={landing_page}")

        def collect_formats(g, dataset_uri, DCT, DCAT):
            # 5.1 formatos diretamente no Dataset
            values = list(g.objects(dataset_uri, DCT["format"]))

            # 5.2 formatos nas Distributions
            for dist in g.objects(dataset_uri, DCAT.distribution):
                # dct:format no distribution
                values.extend(g.objects(dist, DCT["format"]))
                # dcat:mediaType no distribution (muito usado)
                values.extend(g.objects(dist, DCAT.mediaType))

            # normalização de valores (Literal/URI -> string)
            out = []
            for v in values:
                if isinstance(v, Literal):
                    out.append(str(v))
                elif isinstance(v, URIRef):
                    out.append(str(v))  # pode ser um IANA media type como URI
                else:
                    out.append(str(v))
            return out

        raw_formats = collect_formats(g, dataset_uri, DCT, DCAT)

        # Mapeia alguns content-types comuns para "RDF" (para acionar seus bônus em I1/I2/I3)
        RDF_HINTS = (
            "turtle", "rdf+xml", "n-triples", "n-quads", "trig", "json-ld",
            "application/rdf+xml", "text/turtle", "application/ld+json",
            "application/n-triples", "application/n-quads", "application/trig"
        )

        seen = set()
        fmt_list = []
        for fval in raw_formats:
            fv = (fval or "").strip()
            if not fv:
                continue

            # heurística: se parecer media type RDF, adiciona "RDF"
            lower = fv.lower()
            if any(h in lower for h in RDF_HINTS):
                label = "RDF"
                if label not in seen:
                    seen.add(label)
                    fmt_list.append(label)

            # mantém também o valor original (ex.: "Bidirecional Flow", "CSV Files", "Logs")
            if fv not in seen:
                seen.add(fv)
                fmt_list.append(fv)

        fmt_concat = ", ".join(fmt_list) if fmt_list else ""


        app.logger.info(f"[MANUAIS] levelOfmetadata={levelOfmetadata} | availability={availability} | format={fmt_concat}")

        # # =========================
        # # 6) Rodar os FAIR Tests
        # # =========================

        tests_list = data.get("tests", []) or []

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Allow-Control-Allow-Origin": "*",
        }

        # usa Session para keep-alive
        session = requests.Session()

        def do_post(t):
            url = f"https://w3id.org/FAIR_Tests/tests/{t}"
            return t, session.post(url, json=data, headers=headers, timeout=30)

        # controla concorrência sem exagero
        max_workers = min(16, max(4, len(tests_list)))

        # coleta respostas na MESMA ordem de tests_list
        ordered_responses = [None] * len(tests_list)

        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            future_to_idx = {}
            for idx, t in enumerate(tests_list):
                fut = ex.submit(do_post, t)
                future_to_idx[fut] = idx

            for fut in as_completed(future_to_idx):
                idx = future_to_idx[fut]
                try:
                    _t, resp = fut.result()
                    ordered_responses[idx] = resp
                except Exception as e:
                    app.logger.error(f"Erro na requisição para teste '{tests_list[idx]}': {e}")

        response = []
        for idx, test_response in enumerate(ordered_responses):
            if test_response is None:
                app.logger.error(f"Sem resposta para teste '{tests_list[idx]}'")
                continue
            if test_response.status_code == 200:
                try:
                    response.append(test_response.json())
                except ValueError:
                    app.logger.error(
                        f"Erro ao converter resposta para JSON (teste '{tests_list[idx]}'): "
                        f"{test_response.text}"
                    )
            else:
                app.logger.error(
                    f"Erro na requisição (teste '{tests_list[idx]}'): "
                    f"{test_response.status_code} - {test_response.text}"
                )

       
        # =========================
        # 7) Agregar com parâmetros EXTRAÍDOS do RDF
        # =========================
        scores = aggregate_scores_with_manual(
            response,
            levelOfmetadata=levelOfmetadata,  # '0'..'4' (string)
            availability=availability,        # "No" | "On request" | "Yes"
            format=fmt_concat,                 # ex: "Bidirecional Flow, RDF"
            landing_page=landing_page
        )
        app.logger.info(f"SCORES AGREGADOS: {scores}")

        # =========================
        # 8) Retorno
        # =========================
        return jsonify({
            "fair_tests_response": response,
            "aggregate_scores": scores,
            "manual_params": {
                "levelOfmetadata": levelOfmetadata,
                "availability": availability,
                "format": fmt_concat,
                "source": str(dataset_uri),
            }
        }), 200

    except Exception as e:
        app.logger.error(f"FALHOU: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

    
# @app.route("/evaluate", methods=["POST"])
# def evaluate_rdf():
#     data = request.get_json()
#     rdf_text = data.get("dataset")  # <-- Aqui vem o RDF como string
#     doi_request = data.get("doi")  # <-- Aqui vem o DOI como string

#     g = Graph()
#     g.parse(data=rdf_text, format="turtle")

#     # Namespaces
#     DCTERMS = Namespace("http://purl.org/dc/terms/")
#     DCAT = Namespace("http://www.w3.org/ns/dcat#")
#     FDP = Namespace("http://fairdatapoint.org/")
#     TIME = Namespace("http://www.w3.org/2006/time#")
#     OBS = Namespace("https://ontology.unifiedcyberontology.org/uco/observable#")
#     ATHENA = Namespace("http://purl.org/athena-o#")
#     CSRC = Namespace("https://csrc.nist.gov/glossary/")


#     dataset_uri = None
#     for s in g.subjects(RDF.type, DCAT.Dataset):
#         dataset_uri = s
#         break

#     if not dataset_uri:
#         return jsonify({"error": "Dataset URI not found"}), 400

#     def get_value(uri, predicate):
#         value = g.value(subject=uri, predicate=predicate)
#         return str(value).lower() if len(str(value).lower()) > 0 else "not specified"

#     # def get_bool_score(value):
#     #     return 1 if value == "yes" else 0
#     def get_bool_score(value):
#         if isinstance(value, bool):
#             return 1 if value else 0
#         return 1 if str(value).strip().lower() in ["yes", "true"] else 0


#     year = int(g.value(dataset_uri, TIME.year) or 2000)
#     name = g.value(dataset_uri, DCTERMS.title)

#     anonimato = get_value(dataset_uri, CSRC["termanonymity"])
#     print(f"Anonimato: {anonimato}")
#     tipo_trafego = get_value(dataset_uri, ATHENA.kindOfTraffic)
#     public = get_value(dataset_uri, ATHENA.publicAvailability)
#     normal = get_value(dataset_uri, ATHENA.NormalTraffic)
#     attack = get_value(dataset_uri, ATHENA.AttackTraffic)
#     metadata = get_value(dataset_uri, FDP.metadata)  # Esse ainda está válido
#     doi = get_value(dataset_uri, FDP.doi)
#     completo = get_value(dataset_uri, ATHENA.completeNetwork)
#     splits = get_value(dataset_uri, ATHENA.predefinedSplits)
#     balanceado = get_value(dataset_uri, ATHENA.balanced)
#     rotulado = get_value(dataset_uri, ATHENA.labeled)


#     # Scores
#     year_score = yearOfTrafficMetric(year)
#     anonimato_score = anonymityMetric(anonimato, tipo_trafego)
#     public_score = get_bool_score(public)
#     normal_score = get_bool_score(normal)
#     attack_score = get_bool_score(attack)
#     metadata_score = get_bool_score(metadata)
#     complete_score = get_bool_score(completo)
#     split_score = get_bool_score(splits)
#     balance_score = get_bool_score(balanceado)
#     label_score = get_bool_score(rotulado)

#     # Buscar DOI
#     doi_uri = doi_request or g.value(dataset_uri, DCAT.landingPage) or g.value(dataset_uri, DCTERMS.identifier) or doi
#     doi = str(doi_uri).strip().lower() if doi_uri else None
#     if doi and doi.startswith("http"):
#         doi_parts = doi.split("/")
#         doi = "/".join(doi_parts[-2:])

#     citations = get_citations_from_opencitations(doi.upper())
#     relevance_score = relevanceMetric(citations, year_score)

#     scores = [
#         year_score, public_score, normal_score, attack_score, metadata_score,
#         anonimato_score, complete_score, split_score, balance_score, label_score,
#         relevance_score
#     ]

#     fig = radarPlot(scores, name) 

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
#         fig.write_image(tmpfile.name)
#         temp_file_path = tmpfile.name

#         # Salva a imagem em memória (sem gravar no disco)
#     img_bytes = fig.to_image(format="png")
#     img_base64 = base64.b64encode(img_bytes).decode('utf-8')

#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     file_name = f"{name}_{timestamp}.png" if name else f"image_{timestamp}.png"

#     os.remove(temp_file_path)

#     return jsonify({
#         "scores": {
#             "year": year_score,
#             "publicAvailability": public_score,
#             "normalTraffic": normal_score,
#             "attackTraffic": attack_score,
#             "metadata": metadata_score,
#             "anonymity": anonimato_score,
#             "completeNetwork": complete_score,
#             "predefinedSplits": split_score,
#             "balanced": balance_score,
#             "labeled": label_score,
#             "relevance": relevance_score
#         },
#         "imageBase64": f"data:image/png;base64,{img_base64}"
#     })

# -*- coding: utf-8 -*-
from flask import request, jsonify
from rdflib import Graph, Namespace, RDF
from datetime import datetime
import base64, os, tempfile
import plotly.express as px
import pandas as pd

# ====== suas funções de métrica (cole aqui as DEFINIÇÕES que você já tem) ======
# timelinessMetric, availabilityMetric, labelMetric, anonymityMetric,
# relevanceMetric, attackDiversityMetric, normalAndAttackMetric, radarPlot
# (Abaixo, para o servidor, vamos renderizar a figura sem fig.show())

import numpy as np
import skfuzzy as fuzzy
import requests

# ------ Helpers desta versão ------

def normalize_bool_str(v) -> str:
    """
    Converte RDF literal/boolean/string para 'True' ou 'False' (string),
    atendendo as suas funções que esperam strings.
    """
    if v is None:
        return "False"
    s = str(v).strip().lower()
    if s in ("true", "1", "yes"):
        return "True"
    return "False"

def coerce_int(v, default=0):
    try:
        return int(str(v))
    except Exception:
        return default

def network_completeness_metric(text: str) -> float:
    """
    Mapeia o texto de f:completeNetwork para um score em [0..1].
    Heurística simples, pode ajustar depois.
    """
    if not text:
        return 0.0
        # return 0.5
    s = str(text).strip().lower()
    if "single host" in s or "single" in s or "only" in s or "protocols" in s:
        return 0.5
    if "several" in s or "multiple" in s or "routers" in s or "subnet" in s or "hosts" in s:
        return 1.0
    # if "enterprise" in s or "campus" in s or "full" in s or "complete" in s:
    #     return 1.0
    # return 0.5
    return 0.0

def get_text_values(g: Graph, subj, pred):
    """Retorna lista de strings (pode haver múltiplos objetos para o mesmo predicado)."""
    return [str(o) for o in g.objects(subj, pred)]

def get_first_value(g: Graph, subj, pred):
    """Retorna primeiro valor como string (ou None)."""
    for o in g.objects(subj, pred):
        return str(o)
    return None

def normalize_doi(raw):
    if not raw:
        return None
    doi = str(raw).strip()
    # Se vier uma URL, pega o sufixo a/b
    if doi.lower().startswith("http"):
        parts = doi.split("/")
        if len(parts) >= 2:
            doi = "/".join(parts[-2:])
    return doi

def getCitations(doi):
    # Igual ao que você postou (Semantic Scholar)
    if not doi:
        return 0
    api_url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}?fields=title,citationCount"
    try:
        resp = requests.get(api_url, timeout=8)
        if resp.status_code == 200:
            data = resp.json()
            return int(data.get("citationCount", 0))
    except Exception:
        pass
    return 0

def radar_figure(scores_ordered, labels, dataset_name):
    df = pd.DataFrame(dict(r=scores_ordered, theta=labels))
    fig = px.line_polar(df, r="r", theta="theta", line_close=True)
    fig.update_traces(fill="toself")
    fig.update_layout(title=f"Dataset: {dataset_name}")
    return fig

def timelinessMetric(year):
    # This function aims to return the score for the year of the traffic creation property using the triangular
    # membership function of fuzzy logic
    current_year = datetime.now().year

    # range of time of the datasets
    U = np.arange(1998, current_year + 1, 1)

    # Fuzzy sets
    # old_set = fuzzy.trimf(U, [1998, 1998, 2010])
    # medium_set = fuzzy.trimf(U, [2005, 2017, 2020])
    # Recent_set = fuzzy.trimf(U, [2018, current_year + 1, current_year + 1])
    old_set = fuzzy.trimf(U, [1998, 1998, 2010])
    medium_set = fuzzy.trimf(U, [2005, 2017, 2020])
    Recent_set = fuzzy.trimf(U, [2015, current_year + 1, current_year + 1])

    # triangular membership function
    old = fuzzy.interp_membership(U, old_set, year)
    medium = fuzzy.interp_membership(U, medium_set, year)
    Recent = fuzzy.interp_membership(U, Recent_set, year)

    print(f"Old using: {old}")
    print(f"Medium using: {medium}")
    print(f"Recent using: {Recent}")

    if max(old, medium, Recent) == old:
        year_score = 0
    elif max(old, medium, Recent) == medium:
        year_score = 0.5
    elif max(old, medium, Recent) == Recent:
        year_score = 1

    return year_score

def availabilityMetric(availability):
    if availability == "No":
        availability_score = 0
    elif availability == "On request":
        availability_score = 0.5
    elif availability == "Yes":
        availability_score = 1

    return availability_score

def labelMetric(hasLabel):
    if hasLabel == "Unlabeled":
        label_score = 0
    elif hasLabel == "Partially-labeled":
        label_score = 0.5
    elif hasLabel == "Fully-labeled":
        label_score = 1

    return label_score

def anonymityMetric(anonymity, kind_of_Traffic):
    #  This function receives the values of the properties anonymity and kind_of_Traffic and returns the score
    #  for the anonymity. If a dataset has a kindy of traffic Real, it means that the data needs to be anonymized;
    #  otherwise, if the kindy of traffic is emulated or synthetic, it makes no sense for the data to be anonymized.

    if kind_of_Traffic == "Real" and anonymity == "True":
        anonymity_score = 1
    elif kind_of_Traffic == "Real" and anonymity == "False":
        anonymity_score = 0
    elif kind_of_Traffic == "Emulated" and anonymity == "True":
        anonymity_score = 0
    elif kind_of_Traffic == "Emulated" and anonymity == "False":
        anonymity_score = 1
    elif kind_of_Traffic == "Syntethic" and anonymity == "False":
        anonymity_score = 1
    elif kind_of_Traffic == "Syntethic" and anonymity == "True":
        anonymity_score = 0

    return anonymity_score

def relevanceMetric(citations, year_score, reference_value=4500, W=0.3):
    #  Citations is the number of citations of the evaluated dataset. reference_value is the number
    #  of citations considered the maximum, W is the weight considered  for the citations, and Y c is the value
    #  of the score received by the year of traffic creation metric.

        relevance = W * min(citations / reference_value, 1) + (1 - W) * year_score
        return relevance

######################## Specfic Network Intrusion Detection Metrics #################################

def attackDiversityMetric(attackList):
    # attackList é um array com as categorias STRIDE informadas pelo publicador.

    attackDiversityScore = (len(attackList) / 6)

    return round(attackDiversityScore, 2)

def normalAndAttackMetric(normalTraffic, attackTraffic):

    if normalTraffic == "false":
        nt = 0
    else:
        nt = 1

    if attackTraffic == "false":
        at = 0
    else:
        at = 1

    normalAndAttackScore = ((nt + at) / 2)
    return normalAndAttackScore


# =================== ROTA ATUALIZADA ===================

@app.route("/evaluate", methods=["POST"])
def evaluate_rdf():
    data = request.get_json()
    rdf_text = data.get("dataset")

    if not rdf_text:
        return jsonify({"error": "Missing 'dataset' Turtle RDF"}), 400

    g = Graph()
    g.parse(data=rdf_text, format="turtle")

    # Namespaces conforme seu novo RDF
    DCAT = Namespace("http://www.w3.org/ns/dcat#")
    DCT = Namespace("http://purl.org/dc/terms/")
    F = Namespace("http://fairdatapoint.org/")  # prefixo f:
    N1 = Namespace("http://purl.org/athena-o#")  # prefix n1:
    TIME = Namespace("http://www.w3.org/2006/time#")
    GLOSS = Namespace("https://csrc.nist.gov/glossary/")
    # Outros presentes no exemplo, se necessário:
    # FDP = Namespace("https://w3id.org/fdp/fdp-o#")

    # Localiza o dataset (dcat:Dataset)
    dataset_uri = None
    for s in g.subjects(RDF.type, DCAT.Dataset):
        dataset_uri = s
        break

    if not dataset_uri:
        return jsonify({"error": "Dataset URI not found"}), 400

    # ---- Leitura de campos do novo RDF ----
    name = get_first_value(g, dataset_uri, DCT.title) or "Dataset"

    # Timeliness
    year_literal = get_first_value(g, dataset_uri, TIME.yearOfCreation)
    try:
        year = int(year_literal) if year_literal is not None else 2000
    except Exception:
        year = 2000

    # Availability
    availability_txt = get_first_value(g, dataset_uri, GLOSS.termpublicAvailability) or "No"
    availability_txt = availability_txt.strip().title()  # "No" | "On Request" | "Yes"
    # normalizar "On Request" para "On request"
    if availability_txt.lower() == "on request":
        availability_txt = "On request"

    # Anonymization + Kind of traffic
    anonymity_raw = get_first_value(g, dataset_uri, GLOSS.termanonymity)  # true/false
    kind_of_traffic = get_first_value(g, dataset_uri, N1.kindOfTraffic) or ""
    anonymity_str = "True" if str(anonymity_raw).strip().lower() in ("true", "1", "yes") else "False"

    # Labeling
    has_label = get_first_value(g, dataset_uri, N1.hasLabel) or "Unlabeled"

    # Normal / Attack traffic
    normal_raw = get_first_value(g, dataset_uri, N1.normalTraffic)
    attack_raw = get_first_value(g, dataset_uri, N1.attackTraffic)
    normal_str = "True" if str(normal_raw).strip().lower() in ("true", "1", "yes") else "False"
    attack_str = "True" if str(attack_raw).strip().lower() in ("true", "1", "yes") else "False"

    # Network completeness (texto)
    complete_network_txt = get_first_value(g, dataset_uri, F.completeNetwork) or ""

    # Attack diversity:
    # 1) preferir f:attackDiversity (inteiro declarado pelo publisher)
    # f_attack_div = get_first_value(g, dataset_uri, F.attackDiversity)
    # if f_attack_div is not None:
    #     print(f"Usando f:attackDiversity = {f_attack_div}")
    #     print(f"Coerção para int: {coerce_int(f_attack_div, 0)}")
    #     attack_diversity_score = min(max(coerce_int(f_attack_div, 0), 0), 6) / 6.0
    # else:
        # 2) senão, usar cardinalidade de gloss:termattackType
    attack_types = get_text_values(g, dataset_uri, GLOSS.termattackType)
    unique_types = set([t.strip().lower() for t in attack_types if t and t.strip()])
    attack_diversity_score = min(len(unique_types), 6) / 6.0
    # print(f"Attack types encontrados: {unique_types} => score: {attack_diversity_score}") 

    # DOI (prioriza request -> f:doi)
    doi = normalize_doi(get_first_value(g, dataset_uri, F.doi))

    # ---- Cálculo das métricas novas ----
    Timeliness_score = timelinessMetric(year)
    Availability_score = availabilityMetric(availability_txt)
    Anonymization_score = anonymityMetric(anonymity_str, kind_of_traffic)
    Labeling_score = labelMetric(has_label)
    NormalAndAttackTraffic_score = normalAndAttackMetric(normal_str, attack_str)
    NetworkCompleteness_score = network_completeness_metric(complete_network_txt)

    citations = getCitations(doi)
    Relevance = relevanceMetric(citations, Timeliness_score)

    # AttackDiversity já calculado
    AttackDiversity_score = round(attack_diversity_score, 2)

    # Array e labels na nova ordem do seu radarPlot
    labels = [
        "Timeliness", "Availability", "Anonymization", "Labeling",
        "Attack Diversity", "Normal and Attack Traffic",
        "Network Completeness", "Relevance"
    ]
    scores_array = [
        Timeliness_score, Availability_score, Anonymization_score, Labeling_score,
        AttackDiversity_score, NormalAndAttackTraffic_score,
        NetworkCompleteness_score, Relevance
    ]

    # ---- Geração da imagem (sem fig.show() no servidor) ----
    fig = radar_figure(scores_array, labels, name)

    # Salvar/serializar como base64
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        fig.write_image(tmpfile.name)
        temp_file_path = tmpfile.name

    img_bytes = fig.to_image(format="png")
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")
    os.remove(temp_file_path)

    return jsonify({
        "scores": {
            "timeliness": Timeliness_score,
            "availability": Availability_score,
            "anonymization": Anonymization_score,
            "labeling": Labeling_score,
            "attackDiversity": AttackDiversity_score,
            "normalAndAttackTraffic": NormalAndAttackTraffic_score,
            "networkCompleteness": NetworkCompleteness_score,
            "relevance": Relevance,
            "citations": citations,
            "year": year,
        },
        "meta": {
            "dataset": str(dataset_uri),
            "title": name,
            "doi": doi or "",
            "kindOfTraffic": kind_of_traffic,
            "hasLabel": has_label,
            "availabilityRaw": availability_txt,
            "completeNetworkRaw": complete_network_txt,
        },
        "imageBase64": f"data:image/png;base64,{img_base64}"
    })



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=port, debug=True)

