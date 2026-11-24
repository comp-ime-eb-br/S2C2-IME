import numpy as np
import skfuzzy as fuzzy
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime

################## Cybersecurity Datasets Metrics ####################################

def timelinessMetric(year):
    # This function aims to return the score for the year of the traffic creation property using the triangular
    # membership function of fuzzy logic
    current_year = datetime.now().year

    # range of time of the datasets
    U = np.arange(1998, current_year + 1, 1)

    # Fuzzy sets
    old_set = fuzzy.trimf(U, [1998, 1998, 2007])
    medium_set = fuzzy.trimf(U, [2003, 2012, 2019])
    Recent_set = fuzzy.trimf(U, [2016, current_year + 1, current_year + 1])

    # triangular membership function
    old = fuzzy.interp_membership(U, old_set, year)
    medium = fuzzy.interp_membership(U, medium_set, year)
    Recent = fuzzy.interp_membership(U, Recent_set, year)

    print(f"Old: {old}")
    print(f"Medium: {medium}")
    print(f"Recent: {Recent}")

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


#def radarPlot(array,dataset_name):
#    # This function receives an array with 11 positions containing the scores within the range 0 to 1.
#
#    df = pd.DataFrame(dict(
#        r=array,
#        theta=['Year of Traffic Creation', 'Public Availability', 'Normal Traffic', 'Attack Traffic', 'Metadata', 'Anonymity',
#               'Complete Network', 'Predefined Splits', 'Balanced', 'Labeled', 'Relevance']))
#    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
#    fig.update_traces(fill='toself')
#    fig.update_layout(title=f'Dataset: {dataset_name}')
#    fig.show()


def radarPlot(array,dataset_name):
    # This function receives an array with 11 positions containing the scores within the range 0 to 1.

    df = pd.DataFrame(dict(
        r=array,
        theta=['Timeliness', 'Availability', 'Anonymization', 'Labeling', 'Attack Diversity',
               'Normal and Attack Traffic', 'Network Completeness', 'Relevance']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(title=f'Dataset: {dataset_name}')
    fig.show()

def getCitations(doi):
    # Returns the number of citations of an article about the dataset

    api_url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}?fields=title,citationCount"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        citations = data.get('citationCount', 'N/A')
        return citations
    else:
        print("DOI not found in SemanticScholar")

def radarPlotFAIR(array,dataset_name):
    # This function receives an array with 12 positions containing the scores within the range of the FAIR Principles.

    df = pd.DataFrame(dict(
        r=array,
        theta=['F1', 'F2', 'F3', 'A1',
               'A2', 'I1', 'I2', 'I3', 'R1']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True, color_discrete_sequence=['orange'])
    fig.update_traces(fill='toself', line=dict(color='orange'))
    fig.update_layout(title=f'Dataset: {dataset_name}')
    fig.show()

# CIC DDoS 2019
#year = timelinessMetric(2019)
#public_availability = "Yes"
#normal_traffic = 1
#attack_traffic = 1
#metadata = 1
#anonymit = anonymityMetric("none", "emulated")
#complete_network = 1
#predefined_splits = 0
#balanced = 0
#label = 1

Timeliness_score = timelinessMetric(2019)
Availability_score = availabilityMetric("Yes")
Anonymization_score = anonymityMetric("False", "Emulated")
Labeling_score = labelMetric("Fully-labeled")
AttackDiversity_score = attackDiversityMetric(["Denial of Service"])
NormalAndAttackTraffic_score = normalAndAttackMetric("True", "False")
NetworkCompleteness_score = 1

citations = getCitations("10.1109/CCST.2019.8888419")
print("Citações:", citations)
Relevance = relevanceMetric(citations, Timeliness_score)

print(Timeliness_score, Availability_score, Anonymization_score, Labeling_score, AttackDiversity_score, NormalAndAttackTraffic_score,NetworkCompleteness_score,Relevance)
score = [Timeliness_score, Availability_score, Anonymization_score, Labeling_score, AttackDiversity_score, NormalAndAttackTraffic_score,NetworkCompleteness_score,Relevance]
#radarPlot(score, "CICDDoS2019")

################ Avaliação FAIR Findable ######################
# Aqui a idéia e cacular o valor de cada subprincípio de acordo com os resultados do FAIR Metrics mais
# algumas verficações manuais

def f1Metric(gen2_unique_identifier,gen2_data_identifier_persistence,gen2_metadata_identifier_persistence):
    # F1: (meta)data are assigned a globally unique and persistent identifier
    # Precisar ser o Link da distribuição - aqui ele testa o link da propriedade downloadUrl, o publicador
    # precisa ser instruído a preencher esse campo com o link do doi do dataset.
    F1 = (gen2_unique_identifier + gen2_data_identifier_persistence + gen2_metadata_identifier_persistence) / 3
    return F1

def f2Metric(gen2_grounded_metadata, gen2_structured_metadata, levelOfmetadata):
    #  F2: data are described with rich metadata
    # Aqui são realizados testes em dois níveis, o primeiro relacionado aos metadados no FAIR data point através
    # do FAIR Metrics e após a uma autodeclaração do publicador a respeito do nível de completeza dos metadados.
    # a função recebe como parametro o primeiro caracter da string da propriedade Level of completeness and
    # availability of metadata que pode ser (0, 1 , 2 , 3 0u 4), esse valor vai ser normalizado (dividido por 4) e somado
    # com a pontuação do FAIR Metrics.
    levelOfmetadata = int(levelOfmetadata)/4
    F2 = (gen2_grounded_metadata + gen2_structured_metadata + levelOfmetadata)/3
    return F2

def f3Metric(gen2_metadata_identifier_in_metadata,gen2_data_identifier_in_metadata):
    # Principle F3: metadata clearly and explicitly include the identifier of the data it describes
    F3 = (gen2_metadata_identifier_in_metadata + gen2_data_identifier_in_metadata)/2
    return F3

# Principle F4: (meta)data are registered or indexed in a searchable resource
# Fora do escopo no momento
#gen2_searchable = 1
#F4 = gen2_searchable

def a1Metric(gen2_metadata_protocol,gen2_metadata_authorization, availability):
    # inclui testes A1.1 e A1.2 para avaliar metadados
    A11 = gen2_metadata_protocol
    A12 = gen2_metadata_authorization

    # Utiliza a métrica da availability aqui! acho que seria mais interessante
    if availability == "No":
        availability_score = 0
    elif availability == "On request":
        availability_score = 0.5
    elif availability == "Yes":
        availability_score = 1

    A1 = (A11 + A12 + availability_score)/3
    return A1

def a2Metric(gen2_metadata_persistence):
    #  A2: metadata are accessible, even when the data are no longer available
    A2 = gen2_metadata_persistence
    return A2

def i1Metric(gen2_metadata_kr_language_strong,gen2_metadata_kr_language_weak,format):
     # Princípio I1: (meta)dados usam uma linguagem formal, acessível, compartilhada e amplamente aplicável para representação
     # do conhecimento. Ou seja, no caso do dado se ele não esta em RDF ele não cumpre o I1. A opção mais amplamente
     # aceita para aderir a este princípio, atualmente, é o Resource Description Framework (RDF), que é a
     # recomendação do W3C sobre como representar conhecimento na Web em um formato acessível por máquina .
     # Format - PCAP, NetFlow, CSV, JSON, RDF, Others (mudar depois do congresso)
     if "RDF" in format:
         formatScore = 1
     else:
         formatScore = 0
     I1 = (gen2_metadata_kr_language_weak + gen2_metadata_kr_language_strong + formatScore)/3
     return I1

def i2Metric(gen2_metadata_uses_fair_vocabularies_strong,gen2_metadata_uses_fair_vocabularies_weak, format):
    if "RDF" in format:
        formatScore = 1
    else:
        formatScore = 0
    I2 = (gen2_metadata_uses_fair_vocabularies_strong + gen2_metadata_uses_fair_vocabularies_weak + formatScore)/3
    return I2

def i3Metric(gen2_metadata_contains_outward_links, format):
    if "RDF" in format:
        formatScore = 1
    else:
        formatScore = 0
    I3 = (gen2_metadata_contains_outward_links + formatScore)/2
    return I3

def r1Metric(gen2_metadata_includes_license_strong, gen2_metadata_includes_license_weak):
    # R1: (meta)data are richly described with a plurality of accurate and relevant attributes

    # R1.1: (meta)data are released with a clear and accessible data usage license
    R11 = (gen2_metadata_includes_license_weak + gen2_metadata_includes_license_strong)/2

    # R1.2: (meta)dat are associated with detailed provenance - Implementação em andamento

    return R11


# Teste com CIC-DDoS2019 - peguei os resultados do Athena Evaluator manualmente.
F1 = f1Metric(1,1,0)
F2 = f2Metric(1,1,3)
F3 = f3Metric(1,1)
# F4 fora de implementação
A1 = a1Metric(1,1,"Yes")
A2 = a2Metric(0) # Não achei o resultado no Athena Evaluator
I1 = i1Metric(1,1, "CSV")
I2 = i2Metric(0, 1, "CSV")
I3 = i3Metric(1, "CSV")
R1 = r1Metric(1,1)


ArrayFAIR = [F1, F2, F3, A1, A2, I1, I2, I3, R1]

radarPlotFAIR(ArrayFAIR, "CICDDoS2019")




