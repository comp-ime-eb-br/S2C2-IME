from django.shortcuts import render, redirect
from library.views import get_user_current
from room.models import Room
from django.core.files import File
from pathlib import Path
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

#... apps
from library.views import *
from library.categories import *
from recognize.views import *
from classify.views import *
from statistic.views import *
from delivery.views import *
from api.views import api_recognize_entity_by_post, \
api_classify_priority_by_post, api_delivery_message_by_post, api_generate_statistic_by_post

#...
def core_home(request):
    # BLOCK START
    #==================================================================  
    template = context = user_current = None 
    section, title_page, title_sheet = 'core', 'Project', 'Project'
        
    # BLOCK CENTER
    #================================================================== 
    user_current = get_user_current(request.user)
    room_user = Room.objects.all()

    #...
    if not user_current: user = User.objects.get(username='flavio')
    else: user = user_current
    register_audit_user(user, section)

    # BLOCK END
    #==================================================================      
    context  = {'section':section,'title_page':title_page,'title_sheet':title_sheet,
                'user_current':user_current, 'room_user':room_user}        
    template = 'core/content/home/home.html'
    return render (request, template, context)



def message_warning(request):
    # BLOCK START
    #==================================================================  
    template = context = user_current = None 
    section, title_page, title_sheet = 'core', 'Project', 'Project'
        
    # BLOCK CENTER
    #================================================================== 
    message_text = 'We apologize, but the dashboard will be working soon.'
    message_color = 'alert-warning'

    # BLOCK END
    #==================================================================      
    context  = {'section':section,'title_page':title_page,'title_sheet':title_sheet,
                'user_current':user_current,'message_text':message_text,
                'message_color':message_color,}        
    template = 'core/content/home/home.html'
    return render (request, template, context)


#...
def message_login_required(request):
    # BLOCK START
    #==================================================================  
    template = context = user_current = None 
    section, title_page, title_sheet = 'core', 'Project', 'Project'
        
    # BLOCK CENTER
    #================================================================== 
    user_current = get_user_current(request.user)
    room_user = Room.objects.all()
    message_text = 'To access the chat rooms you need to log in.'
    message_color = 'alert-warning'
    message_signup = None

    # BLOCK END
    #==================================================================      
    context  = {'section':section,'title_page':title_page,'title_sheet':title_sheet,
                'user_current':user_current,'room_user':room_user, 'message_text':
                message_text, 'message_color':message_color,'message_signup':message_signup,}        
    template = 'core/content/home/home.html'
    return render (request, template, context)


#...
def make_processing_recognize_entity(message_raw=None):  

    message_tokens, len_tokens, lst_ents_posi, lst_ents_text, lst_ents_kind, \
    list_message_ents, dict_message_ents, count_ents, message_with_ents = \
    recognize_get_entity_message(message_raw)

    message_priority = classify_make_priority_message(message_raw, count_ents, \
                                                      message_tokens)
    
    background_message, color_border_message, weight_border_message, \
    highlight_text_message = make_delivery_message(message_raw)    

    statistic_make_dictionary_message(context)    

    return context

    # BLOCK INIT
    #==================================================================  
    message_with_ents, message_sentiment, len_sent, lst_sent = '', None, None, None
    ents_name, ents_kind, ents_init, ents_end, list_message_ents = [],[],[],[],[]
    noun_count = verb_count = pron_count = adje_count = punc_count = adve_count = 0
    conj_count = det_count = other_count = count_ents = num_count = 0
    lst_noun, lst_verb, lst_adve, lst_pron, lst_adje, lst_punc, lst_conj, lst_det,\
    lst_num, lst_other, len_sent, lst_sent  = [],[],[],[],[],[],[],[],[],[],[],[]


    # BLOCK MAIN
    #==================================================================  
    #... CONTAINER MAIN START PROCESSING ...#
    message_raw, start_processing, date = library_main_start_processing(message_raw)


    #print("\n\n\nentered recognize...")
    #... CONTAINER RECOGNIZE ENTITY - 192.168.91.65:8002 ...#
    message_tokens, len_tokens, lst_ents_posi, lst_ents_text, lst_ents_kind, list_message_ents, \
    dict_message_ents, count_ents, message_with_ents = \
    recognize_get_entity_message(message_raw) #api_recognize_entity_by_post(message_raw) 
    #print("exited recognize...\n")


    #print("\nentered classify...")
    #... CONTAINER CLASSIFY PRIORITY - 192.168.91.69:8003 ...#
    message_priority = \
    classify_make_priority_message(message_raw, count_ents, message_tokens)
    #api_classify_priority_by_post(message_raw, count_ents, message_tokens)
    #print("exited classify...\n")


    #print("\nentered delivery...")
    #... CONTAINER DELIVERY MESSAGE - 192.168.91.70:8004 ...#
    background_message, color_border_message, weight_border_message, highlight_text_message = \
    make_delivery_message(message_raw)
    #api_delivery_message_by_post(message_raw)
    #print("exited delivery...\n")

    #print("\nentered finish...")
    #... CONTAINER MAIN FINISH PROCESSING 192.168.91.62:8001 ...#
    finish_processing, time_processing, finish_processing, start_processing = \
    library_main_finish_processing(start_processing)
    #print("exited finish...\n")


    #... CONTAINER GENERATE STATISTICS - 192.168.91.71:8005 ...#
    # host_sender, ip_sender,host_receiver, ip_receiver, noun_count, verb_count, pron_count, adje_count, \
    # punc_count, num_count, adve_count,conj_count,det_count, other_count, lst_noun, lst_verb, lst_adve, \
    # lst_pron, lst_adje, lst_punc, lst_conj, lst_det, lst_num, lst_other = \
    #api_generate_statistic_by_post(message_raw)

    #print(f'message new : {message_tokens}\n\n\n')


    # BLOCK END
    #==================================================================  
    context = {'ents_name':ents_name,'ents_kind':ents_kind,'ents_init':ents_init,'ents_end':ents_end,
    'message_with_ents':message_with_ents,'message_raw':message_raw,'message_tokens':message_tokens,
    'len_tokens':len_tokens,'date':date,'lst_ents_posi':lst_ents_posi,'lst_ents_text':lst_ents_text,
    'lst_ents_kind':lst_ents_kind,'dict_message_ents':dict_message_ents,'start_processing':start_processing,
    'message_priority':message_priority,'finish_processing':finish_processing,'time_processing':time_processing,
    'message_sentiment':message_sentiment,'list_message_ents':list_message_ents,'len_sent':len_sent,
    'lst_sent':lst_sent,'background_message':background_message,'color_border_message':color_border_message,
    'weight_border_message':weight_border_message, 'highlight_text_message':highlight_text_message,
    }

    #statistic_make_dictionary_message(context)

    #print(context,"\n\n\n")

    return context
