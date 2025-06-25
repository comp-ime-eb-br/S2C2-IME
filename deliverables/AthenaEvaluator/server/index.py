from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import base64
from fair_processor import aggregate_scores, generate_radar_chart, upload_to_imagekit
from datetime import datetime
from ATHENA_evaluation_metrics import (
    yearOfTrafficMetric,
    anonymityMetric,
    relevanceMetric,
    radarPlot,
    get_citations_from_opencitations
)
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF
import tempfile
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route('/proxy', methods=['POST'])
def proxy():
    data = request.get_json()
    app.logger.info(data.get("tests"))
    app.logger.info("PROXY")
    app.logger.info("data:")
    app.logger.info(data.get("subject"))
    
    try:
        test_responses = [
            requests.post(
                f"https://w3id.org/FAIR_Tests/tests/{t}",
                json=data,
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "Allow-Control-Allow-Origin": "*",
                }
            ) for t in data.get("tests", [])
        ]
        
        app.logger.info(f"TEST RESPONSES: {test_responses}")

        # Verificar se a resposta é válida antes de processar
        response = []
        for test_response in test_responses:
            if test_response.status_code == 200:
                try:
                    response.append(test_response.json())
                except ValueError:
                    app.logger.error(f"Erro ao converter resposta para JSON: {test_response.text}")
            else:
                app.logger.error(f"Erro na requisição: {test_response.status_code} - {test_response.text}")
        
        app.logger.info(f"JSON RESPONSE: {response}")
        return jsonify(response), 200
    except Exception as e:
        app.logger.error(f"FALHOU: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    
@app.route('/generate-graph', methods=['POST'])
def generate_graph():
    try:
        response = request.get_json()

        # 1. Calcular scores
        scores = aggregate_scores(response)


        # 2. Gerar imagem temporária
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:

            generate_radar_chart(scores, tmpfile.name)

        # 3. Fazer upload usando variáveis de ambiente

        image_url = upload_to_imagekit(
            local_file_path=tmpfile.name,
            file_name=os.path.basename(tmpfile.name),
            public_key=os.environ["IMAGEKIT_PUBLIC_KEY"],
            private_key=os.environ["IMAGEKIT_PRIVATE_KEY"],
            url_endpoint=os.environ["IMAGEKIT_URL_ENDPOINT"]
        )
        app.logger.info(image_url)

        

        return jsonify({"url": image_url}), 200

    except Exception as e:
        app.logger.error(f"Erro ao gerar gráfico: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/evaluate", methods=["POST"])
def evaluate_rdf():
    data = request.get_json()
    rdf_text = data.get("dataset")  # <-- Aqui vem o RDF como string
    doi_request = data.get("doi")  # <-- Aqui vem o DOI como string

    g = Graph()
    g.parse(data=rdf_text, format="turtle")

    # Namespaces
    DCTERMS = Namespace("http://purl.org/dc/terms/")
    DCAT = Namespace("http://www.w3.org/ns/dcat#")
    FDP = Namespace("http://fairdatapoint.org/")
    TIME = Namespace("http://www.w3.org/2006/time#")
    OBS = Namespace("https://ontology.unifiedcyberontology.org/uco/observable#")

    dataset_uri = None
    for s in g.subjects(RDF.type, DCAT.Dataset):
        dataset_uri = s
        break

    if not dataset_uri:
        return jsonify({"error": "Dataset URI not found"}), 400

    def get_value(uri, predicate):
        value = g.value(subject=uri, predicate=predicate)
        return str(value).lower() if value else "not specified"

    def get_bool_score(value):
        return 1 if value == "yes" else 0

    year = int(g.value(dataset_uri, TIME.year) or 2000)
    anonimato = get_value(dataset_uri, FDP.anonimity)
    tipo_trafego = get_value(dataset_uri, FDP.kindOfTraffic)
    public = get_value(dataset_uri, FDP.publicAvailability)
    # normal = get_value(dataset_uri, URIRef("http://fairdatapoint.org/normalTraffic"))
    normal = get_value(dataset_uri, OBS.NetworkFlow)
    # attack = get_value(dataset_uri, URIRef("http://fairdatapoint.org/attackTraffic"))
    attack = get_value(dataset_uri, OBS.NetworkFlow)
    metadata = get_value(dataset_uri, FDP.metadata)
    completo = get_value(dataset_uri, FDP.completeNetwork)
    splits = get_value(dataset_uri, FDP.predefinedSplits)
    balanceado = get_value(dataset_uri, FDP.balanced)
    rotulado = get_value(dataset_uri, FDP.labeled)
    name = g.value(dataset_uri, DCTERMS.title)

    # Scores
    year_score = yearOfTrafficMetric(year)
    anonimato_score = anonymityMetric(anonimato, tipo_trafego)
    public_score = get_bool_score(public)
    normal_score = get_bool_score(normal)
    attack_score = get_bool_score(attack)
    metadata_score = get_bool_score(metadata)
    complete_score = get_bool_score(completo)
    split_score = get_bool_score(splits)
    balance_score = get_bool_score(balanceado)
    label_score = get_bool_score(rotulado)

    # Buscar DOI
    doi_uri = doi_request or g.value(dataset_uri, DCAT.landingPage) or g.value(dataset_uri, DCTERMS.identifier)
    doi = str(doi_uri).strip().lower() if doi_uri else None
    if doi and doi.startswith("http"):
        doi_parts = doi.split("/")
        doi = "/".join(doi_parts[-2:])

    citations = get_citations_from_opencitations(doi.upper())
    relevance_score = relevanceMetric(citations, year_score)

    scores = [
        year_score, public_score, normal_score, attack_score, metadata_score,
        anonimato_score, complete_score, split_score, balance_score, label_score,
        relevance_score
    ]

    fig = radarPlot(scores, name) 

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        fig.write_image(tmpfile.name)
        temp_file_path = tmpfile.name

        # Salva a imagem em memória (sem gravar no disco)
    img_bytes = fig.to_image(format="png")
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{name}_{timestamp}.png" if name else f"image_{timestamp}.png"

    # imageurl = upload_to_imagekit(
    #     local_file_path=temp_file_path,
    #     file_name=file_name,
    #     public_key=os.environ["IMAGEKIT_PUBLIC_KEY"],
    #     private_key=os.environ["IMAGEKIT_PRIVATE_KEY"],
    #     url_endpoint=os.environ["IMAGEKIT_URL_ENDPOINT"]
    # )

    # app.logger.info(f"Image URL: {imageurl}")

    os.remove(temp_file_path)

    return jsonify({
        "scores": {
            "year": year_score,
            "publicAvailability": public_score,
            "normalTraffic": normal_score,
            "attackTraffic": attack_score,
            "metadata": metadata_score,
            "anonymity": anonimato_score,
            "completeNetwork": complete_score,
            "predefinedSplits": split_score,
            "balanced": balance_score,
            "labeled": label_score,
            "relevance": relevance_score
        },
        "imageBase64": f"data:image/png;base64,{img_base64}"
        # "imageurl": imageurl,
    })

import base64
import os
import tempfile
from flask import request, jsonify
from imagekitio import ImageKit

@app.route("/upload-image", methods=["POST"])
def upload_image():
    try:
        data = request.get_json()
        image_base64 = data.get("image")
        name = data.get("name")
        file_name = data.get("fileName", "athena_image_upload.png")

        if not image_base64:
            return jsonify({"error": "Imagem em base64 não fornecida."}), 400

        # Remove prefixo se existir (ex: data:image/png;base64,...)
        if "," in image_base64:
            image_base64 = image_base64.split(",")[1]

        image_bytes = base64.b64decode(image_base64)

        # Salva temporariamente o arquivo
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_file.write(image_bytes)
            temp_file_path = temp_file.name

        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{name}_{timestamp}.png" if name else f"image_{timestamp}.png"

        imageurl = upload_to_imagekit(
            local_file_path=temp_file_path,
            file_name=file_name,
            public_key=os.environ["IMAGEKIT_PUBLIC_KEY"],
            private_key=os.environ["IMAGEKIT_PRIVATE_KEY"],
            url_endpoint=os.environ["IMAGEKIT_URL_ENDPOINT"]
        )

        app.logger.info(f"Image URL: {imageurl}")
        # Remove o arquivo local temporário
        os.remove(temp_file_path)

        return jsonify({"url": imageurl})

    except Exception as e:
        app.logger.error(f"Erro ao fazer upload da imagem: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
