from django.shortcuts import render
from django.core.files import File
from pathlib import Path
from library.views import load_priority_words, load_priority_simbols,\
load_interrogative_pronouns
from library.categories import *
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


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def classify_make_priority_message(*args):

    _message_priority = classify_get_classify_priority_message(args[0], int(args[1]))
    #_sentiment_kind = classify_get_sentiment_anlisys_message(list(args[2]))
    #_len_sent, _lst_sent = classify_get_sentence_message(args[0])

    return _message_priority #, _sentiment_kind, None, None #_len_sent, _lst_sent


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def classify_get_classify_priority_message(*args):

    message_raw, count_ents = args[0], int(args[1])
    interrogation = load_priority_simbols()

    message_priority = True if count_ents > 3 or interrogation in message_raw else False

    return message_priority

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def classify_get_sentiment_anlisys_message(*args): 

    sentiment_kind, good_sentiments, bad_sentiments = 'Neutral', 0, 0
    good_sentiments, bad_sentiments = load_term_sentiment_analisys()

    for __, _ in enumerate(range(0,len(args[0]))):
        if args[0][_] in good_sentiments: 
            sentiment_kind = 'Good, because he says ' + str(args[0][_]).upper()
        elif args[0][_] in bad_sentiments: 
            sentiment_kind = 'Bad, because he says ' + str(args[0][_]).upper()
     
    return sentiment_kind

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def classify_get_sentence_message(*args):

    nlp = load_nlp()[1]
    lst_sent, doc = [], nlp(args[0])

    for sent in doc.sents:
        lst_sent.append(sent)
    len_sent = len(lst_sent)

    return len_sent, lst_sent


