from django.shortcuts import render
from django.core.files import File
from pathlib import Path
from library.views import get_acronym_kind_ents, get_sentiment_anlisys_message, \
get_entities_c2_message, get_count_grammar_message, get_classify_priority_message, \
make_message_with_ents, get_user_current, make_list_with_properties_ents, \
make_list_with_grammar_message, get_sentence_message, get_time_processing, \
get_host_and_ip_sender, get_host_and_ip_receiver, get_tokens_at_message
from library.categories import load_nlp
import spacy
from spacy import displacy
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.util import ngrams
import re
import json
from datetime import datetime
import numpy as np
from time import process_time
import os
import requests

#...
def delivery_home(request):
    pass


#---------------------------------------------------
# flavio. make a table with the elements of the message
#---------------------------------------------------
def make_table_output(message=None):   
    table_entity = BeautifulTable()
    doc_entity = nlp(message)

    table_entity.columns.header = ['ENTIDADE', 'TIPO', 'POSITION', 'START', 'END', ]

    for __, _ in enumerate(doc_entity.ents): 
        table_entity.rows.append([_.text, _.label_, __, _.start_char, _.end_char])

    return table_entity


#---------------------------------------------------
# flavio. Render the result to browser
#---------------------------------------------------
def render_result_to_web(doc):
    colors = {
        "ACTION"    : '#00FFFF',
        "DIRECTION" : '#CCCCFF',
        "EQUIPAMENT": '#D35400',
        "MEMBER"    : '#F1C40F',
        "PLACE"     : '#1ABC9C',
        "UNIT"      : '#3498DB',
        "VEHICLE"   : '#9B59B6',
        "WEAPONS"   : '#E74C3C',
        "ACTION"    : '#ca3ce7',
        "ORGANIZATION":'#3ce1e7'}
    
    options = {"ents": ["ACTION","DIRECTION",
                "EQUIPAMENT","MEMBER",
                "PLACE","UNIT","ORGANIZATION",
                "VEHICLE","WEAPONS",],
                "colors": colors}
    
    render_entity_ux = displacy.serve(doc, style="ent", auto_select_port=True, options=options)   

    return render_entity_ux


def make_delivery_message(*args):

    background_message     = 'alert alert-danger'
    color_border_message   = 'border border-danger'
    weight_border_message  = 'border-2'
    highlight_text_message = 'success'
    
    return background_message,color_border_message,weight_border_message,highlight_text_message