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
        theta=['F1', 'F2', 'F3', 'F4', 'A1.1', 'A1.2',
               'A2', 'I1', 'I2', 'I3', 'R1.1', 'R1.2']))
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
radarPlot(score, "CICDDoS2019")

# Avaliação FAIR Findable
gen2_unique_identifier = 1
gen2_metadata_identifier_persistence = 1
F1 = (gen2_unique_identifier + gen2_metadata_identifier_persistence)/2

gen2_grounded_metadata = 1
gen2_structured_metadata = 1
F2 = (gen2_grounded_metadata + gen2_structured_metadata)/2

gen2_metadata_identifier_in_metadata = 1
gen2_data_identifier_in_metadata = 1
F3 = (gen2_metadata_identifier_in_metadata + gen2_data_identifier_in_metadata)/2

gen2_searchable = 1
F4 = gen2_searchable

# Avaliação FAIR Accessible
gen2_metadata_protocol = 1
A11 = gen2_metadata_protocol

gen2_metadata_authorization = 1
A12 = gen2_metadata_authorization

gen2_metadata_persistence = 0
manual_estarNoFDP = 1
A2 = (gen2_metadata_persistence + manual_estarNoFDP)/2

# Avaliação FAIR Interoperable
gen2_metadata_kr_language_strong = 1
gen2_metadata_kr_language_weak = 1
I1 = (gen2_metadata_kr_language_weak + gen2_metadata_kr_language_strong)/2

gen2_metadata_uses_fair_vocabularies_strong = 0
gen2_metadata_uses_fair_vocabularies_weak = 1
I2 = (gen2_metadata_uses_fair_vocabularies_strong + gen2_metadata_kr_language_weak)/2

gen2_metadata_contains_outward_links = 1
I3 = gen2_metadata_contains_outward_links

# Avaliação FAIR reusable
gen2_metadata_includes_license_strong = 1
gen2_metadata_includes_license_weak = 1
R11 = (gen2_metadata_includes_license_weak + gen2_metadata_includes_license_strong)/2

R12 = 1 # manual

ArrayFAIR = [F1, F2, F3, F4, A11, A12, A2, I1, I2, I3, R11, R12]

#radarPlotFAIR(ArrayFAIR, "CICDDoS2019")





