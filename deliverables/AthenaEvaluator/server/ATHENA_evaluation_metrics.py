import numpy as np
import skfuzzy as fuzzy
import plotly.express as px
import pandas as pd
from datetime import datetime
import requests

def yearOfTrafficMetric(year):
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


def anonymityMetric(anonymity, kind_of_Traffic):
    #  This function receives the values of the properties anonymity and kind_of_Traffic and returns the score
    #  for the anonymity. If a dataset has a kindy of traffic Real, it means that the data needs to be anonymized;
    #  otherwise, if the kindy of traffic is emulated or synthetic, it makes no sense for the data to be anonymized.

    if kind_of_Traffic == "real" and anonymity == "yes":
        anonymity_score = 1
    elif kind_of_Traffic == "real" and anonymity == "none":
        anonymity_score = 0
    elif anonymity == "not specified":
        anonymity_score = 0
    elif kind_of_Traffic == "emulated" and anonymity == "yes":
        anonymity_score = 0
    elif kind_of_Traffic == "emulated" and anonymity == "none":
        anonymity_score = 1
    elif kind_of_Traffic == "syntethic" and anonymity == "none":
        anonymity_score = 1
    elif kind_of_Traffic == "syntethic" and anonymity == "yes":
        anonymity_score = 0

    return anonymity_score

def relevanceMetric(citations, year_score, reference_value=4000, W=0.3):
    #  Citations is the number of citations of the evaluated dataset. reference_value is the number
    #  of citations considered the maximum, W is the weight considered  for the citations, and Y c is the value
    #  of the score received by the year of traffic creation metric.
    
    relevance = W * min(citations / reference_value, 1) + (1 - W) * year_score
    return relevance

def radarPlot(array,dataset_name):
    # This function receives an array with 11 positions containing the scores within the range 0 to 1.

    df = pd.DataFrame(dict(
        r=array,
        theta=['Year of Traffic Creation', 'Public Availability', 'Normal Traffic', 'Attack Traffic', 'Metadata', 'Anonymity',
               'Complete Network', 'Predefined Splits', 'Balanced', 'Labeled', 'Relevance']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(title=f'Dataset: {dataset_name}')
    # fig.show()

    return fig  # Retorna o objeto fig para uso posterior, se necessário

def get_citations_from_opencitations(doi: str) -> int:
    print(f"Fetching citations for DOI: {doi}")
    try:
        response = requests.get(f"https://opencitations.net/index/api/v2/citation-count/doi:{doi}")
        if response.status_code == 200:
            data = response.json()
            citations = int(data[0]["count"])
            return citations
    except Exception as e:
        print(f"Erro ao buscar citações: {e}")
    return 0  # fallback se falhar

