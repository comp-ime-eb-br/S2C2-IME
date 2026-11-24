# fair_processor.py
from collections import defaultdict
from math import pi
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# ========= Mapas e utilidades =========

TESTS_INFO = {
    "gen2_unique_identifier": {"label": "F1", "principle": "F"},
    "gen2_data_identifier_persistence": {"label": "F1", "principle": "F"},
    "gen2_metadata_identifier_persistence": {"label": "F1", "principle": "F"},
    "gen2_grounded_metadata": {"label": "F2", "principle": "F"},
    "gen2_structured_metadata": {"label": "F2", "principle": "F"},
    "gen2_data_identifier_in_metadata": {"label": "F3", "principle": "F"},
    "gen2_metadata_identifier_in_metadata": {"label": "F3", "principle": "F"},

    "gen2_metadata_protocol": {"label": "A1.1", "principle": "A"},
    "gen2_metadata_authorization": {"label": "A1.2", "principle": "A"},
    "gen2_metadata_persistence": {"label": "A2", "principle": "A"},

    "gen2_metadata_kr_language_strong": {"label": "I1", "principle": "I"},
    "gen2_metadata_kr_language_weak": {"label": "I1", "principle": "I"},
    "gen2_metadata_uses_fair_vocabularies_strong": {"label": "I2", "principle": "I"},
    "gen2_metadata_uses_fair_vocabularies_weak": {"label": "I2", "principle": "I"},
    "gen2_metadata_contains_outward_links": {"label": "I3", "principle": "I"},

    "gen2_metadata_includes_license_strong": {"label": "R1.1", "principle": "R"},
    "gen2_metadata_includes_license_weak": {"label": "R1.1", "principle": "R"},
}

def _parse_test_scores(response):
    """
    Lê a `response` do FAIR Metrics (mesmo formato que você já usa) e
    retorna um dicionário { test_name: score_float }.
    """
    scores_by_test = {}
    for metric_group in response:
        if not metric_group or not isinstance(metric_group, list):
            continue
        metric = metric_group[0]
        metric_id = metric.get("@id", "")
        test_name = metric_id.split("/tests/")[-1].split("#")[0]
        try:
            score = float(metric["http://semanticscience.org/resource/SIO_000300"][0]["@value"])
        except Exception:
            score = 0.0  # fallback seguro
        scores_by_test[test_name] = score
    return scores_by_test

# ========= Suas funções de subprincípio =========

def f1Metric(gen2_unique_identifier, gen2_data_identifier_persistence, gen2_metadata_identifier_persistence):
    return (gen2_unique_identifier + gen2_data_identifier_persistence + gen2_metadata_identifier_persistence) / 3

def f2Metric(gen2_grounded_metadata, gen2_structured_metadata, levelOfmetadata):
    levelOfmetadata = int(levelOfmetadata) / 4
    return (gen2_grounded_metadata + gen2_structured_metadata + levelOfmetadata) / 3

def f3Metric(gen2_metadata_identifier_in_metadata, gen2_data_identifier_in_metadata):
    return (gen2_metadata_identifier_in_metadata + gen2_data_identifier_in_metadata) / 2

def a1Metric(gen2_metadata_protocol, gen2_metadata_authorization, availability):
    # if availability == "No":
    #     availability_score = 0
    # elif availability == "On request":
    #     availability_score = 0.5
    # elif availability == "Yes":
    #     availability_score = 1
    # else:
    #     availability_score = 0  # fallback

    return (gen2_metadata_protocol + gen2_metadata_authorization) / 2

def a2Metric(gen2_metadata_persistence):
    return gen2_metadata_persistence

def i1Metric(gen2_metadata_kr_language_strong, gen2_metadata_kr_language_weak, format):
    if "RDF" in format  or "TTL" in format or "OWL" in format: # Nível máximo de interoperabilidade
         formatScore = 1
    else:
         formatScore = 0
    # formatScore = 1 if ("RDF" in (format or "")) else 0
    return (gen2_metadata_kr_language_weak + gen2_metadata_kr_language_strong + formatScore) / 3

def i2Metric(gen2_metadata_uses_fair_vocabularies_strong, gen2_metadata_uses_fair_vocabularies_weak, format):
    print("Format recebido em i2Metric:", format)
    if "RDF" in format  or "TTL" in format or "OWL" in format:
        formatScore = 1
    else:
        formatScore = 0
    # formatScore = 1 if ("RDF" in (format or "")) else 0
    return (gen2_metadata_uses_fair_vocabularies_strong + gen2_metadata_uses_fair_vocabularies_weak + formatScore) / 3

def i3Metric(gen2_metadata_contains_outward_links, format):
    # formatScore = 1 if ("RDF" in (format or "")) else 0
    return (gen2_metadata_contains_outward_links)

def r1Metric(gen2_metadata_includes_license_strong, gen2_metadata_includes_license_weak, landing_page):
    # R1: (meta)data are richly described with a plurality of accurate and relevant attributes

    # R1.1: (meta)data are released with a clear and accessible data usage license
    R11 = (gen2_metadata_includes_license_weak + gen2_metadata_includes_license_strong)/2

    # R1.2: (meta)dat are associated with detailed provenance - Implementação em andamento
    if isinstance(landing_page, str) and landing_page.strip() != "":
        R12 = 1
    else:
        R12 = 0
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa R12:", R12)
    R1 = (R11 + R12)/2

    return R1
    # return (gen2_metadata_includes_license_weak + gen2_metadata_includes_license_strong) / 2  # R1.1

# ========= Agregador novo (response + parâmetros manuais) =========

def aggregate_scores_with_manual(
    response,
    *,
    levelOfmetadata: str,
    availability: str,
    format: str,
    landing_page: str,
):
    """
    Calcula os subprincípios e as médias por princípio (F, A, I, R)
    usando:
      - a mesma `response` do FAIR Metrics que você já recebe
      - parâmetros manuais: `levelOfmetadata`, `availability`, `format`

    Retorna:
    {
      "subprinciples": {"F1":..., "F2":..., "F3":..., "A1":..., "A2":..., "I1":..., "I2":..., "I3":..., "R1.1":...},
      "principles":    {"F":..., "A":..., "I":..., "R":...},
      "raw_tests":     {<test_name>: <score>, ...}
    }
    """
    t = _parse_test_scores(response)

    # Helper para pegar teste com default 0.0 se ausente
    g = lambda name: float(t.get(name, 0.0))

    # ---- Subprincípios ----
    F1 = f1Metric(
        g("gen2_unique_identifier"),
        g("gen2_data_identifier_persistence"),
        g("gen2_metadata_identifier_persistence"),
    )

    F2 = f2Metric(
        g("gen2_grounded_metadata"),
        g("gen2_structured_metadata"),
        levelOfmetadata,
    )

    F3 = f3Metric(
        g("gen2_metadata_identifier_in_metadata"),
        g("gen2_data_identifier_in_metadata"),
    )

    A1 = a1Metric(
        g("gen2_metadata_protocol"),
        g("gen2_metadata_authorization"),
        availability,
    )

    A2 = a2Metric(
        g("gen2_metadata_persistence")
    )

    I1 = i1Metric(
        g("gen2_metadata_kr_language_strong"),
        g("gen2_metadata_kr_language_weak"),
        format,
    )

    I2 = i2Metric(
        g("gen2_metadata_uses_fair_vocabularies_strong"),
        g("gen2_metadata_uses_fair_vocabularies_weak"),
        format,
    )

    I3 = i3Metric(
        g("gen2_metadata_contains_outward_links"),
        format,
    )

    R11 = r1Metric(
        g("gen2_metadata_includes_license_strong"),
        g("gen2_metadata_includes_license_weak"),
        landing_page,
    )

    subprinciples = {
        "F1": F1, "F2": F2, "F3": F3,         # (F4 fora do escopo)
        "A1": A1, "A2": A2,
        "I1": I1, "I2": I2, "I3": I3,
        "R1": R11,
    }

    # ---- Médias por princípio ----
    # F = média(F1, F2, F3)   (F4 fora do escopo no momento)
    F_mean = (F1 + F2 + F3) / 3

    # A = média(A1, A2)
    A_mean = (A1 + A2) / 2

    # I = média(I1, I2, I3)
    I_mean = (I1 + I2 + I3) / 3

    # R = aqui só R1.1 por enquanto
    R_mean = R11

    principles = {
        "F": F_mean,
        "A": A_mean,
        "I": I_mean,
        "R": R_mean,
    }

    return {
        "subprinciples": subprinciples,
        "principles": principles,
        "raw_tests": t,
    }

# ========= Gráfico radar (aceita qualquer dicionário label->score) =========

def generate_radar_chart(scores_dict, output_path, label_order=None, title=None):
    """
    Plota um radar para um dicionário {label: score}.
    - `label_order`: opcional, força a ordem dos eixos (ex.: ["F1","F2","F3","A1","A2","I1","I2","I3","R1.1"])
    - `title`: opcional, título no gráfico
    """
    if not scores_dict:
        raise ValueError("scores_dict vazio")

    categories = label_order or list(scores_dict.keys())
    values = [float(scores_dict.get(k, 0.0)) for k in categories]
    values += values[:1]

    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    fig = plt.figure()
    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1], categories, color='grey', size=8)
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75, 1], ["0.25", "0.5", "0.75", "1"], color="grey", size=7)
    plt.ylim(0, 1)

    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)

    if title:
        plt.title(title, pad=20)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)
