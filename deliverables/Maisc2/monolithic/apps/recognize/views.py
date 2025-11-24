from django.shortcuts import render
from django.core.files import File
from pathlib import Path
from library.views import *
from library.categories import *
from library.views import remove_accent_word
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

#...
def recognize_get_entity_message(args):

    #print("entered reconize 2")

    _doc_message = recognize_load_nlp_maisc2(args)
    _message_tokens, _len_tokens = recognize_get_tokens_at_message(args)
    _lst_ents_posi, _lst_ents_text, _lst_ents_kind = recognize_make_list_with_properties_ents(_message_tokens)
    _list_message_ents, _dict_message_ents, _count_ents = recognize_get_entities_c2_message(_doc_message)
    _message_with_ents = recognize_make_message_with_ents(_list_message_ents)

    return _message_tokens, _len_tokens, _lst_ents_posi, _lst_ents_text, _lst_ents_kind, \
    _list_message_ents, _dict_message_ents, _count_ents, _message_with_ents

#...
def recognize_load_nlp_maisc2(args):
    nlp_maisc2 = load_nlp()[0]
    doc_message = nlp_maisc2(args) 

    return doc_message

#...
def recognize_get_tokens_at_message(*args):
    token = TreebankWordTokenizer()
    message_tokens = token.tokenize(args[0])
    len_tokens = str(len(message_tokens))

    return message_tokens, len_tokens    

#... 
def recognize_make_list_with_properties_ents(*args):
    act, agt, drt, wep, unt, vhc, plc = load_categ_ents_c2()
    lst_ents_posi,lst_ents_text,lst_ents_kind = [],[],[]

    for __, _ in enumerate(args[0]): 
        _ = remove_accent_word(_)
        if   _ in act:
            lst_ents_posi.append(__)
            lst_ents_text.append(_)
            lst_ents_kind.append('ACT')
        elif _ in agt:
            lst_ents_posi.append(__)
            lst_ents_text.append(_)
            lst_ents_kind.append('AGT')
        elif _ in drt:
            lst_ents_posi.append(__)
            lst_ents_text.append(_)
            lst_ents_kind.append('DRT')
        elif _ in wep:
            lst_ents_posi.append(__)
            lst_ents_text.append(_)
            lst_ents_kind.append('WEP')
        elif _ in unt:
            lst_ents_posi.append(__)
            lst_ents_text.append(_)
            lst_ents_kind.append('UNT')
        elif _ in vhc:
            lst_ents_posi.append(__)
            lst_ents_text.append(_)
            lst_ents_kind.append('VHC')
        elif _ in plc:
            lst_ents_posi.append(__)
            lst_ents_text.append(_)
            lst_ents_kind.append('PLC')
            
    return lst_ents_posi, lst_ents_text, lst_ents_kind

#...
def recognize_get_entities_c2_message(args):
    dic, message_ents, count_ents = {}, [], 0
    doc_message = args
    
    list_categ_ents_c2 = load_categ_ents_c2()

    #...
    for __, _ in enumerate(doc_message):
        word = remove_accent_word(_.text)
        if word in list_categ_ents_c2[0]: 
            message_ents.append(f"{_.text} [ACT]")
            dic[__]={'value':f' {_.text} [ACT]', 'bgcolor':'#00FFFF', 'color':'#000'}
            count_ents+=True
        elif word in list_categ_ents_c2[1]: 
            message_ents.append(f"{_.text} [AGT]")
            dic[__]={'value':f' {_.text} [AGT]', 'bgcolor':'#F1C40F', 'color':'#000'}
            count_ents+=True
        elif word in list_categ_ents_c2[2]: 
            message_ents.append(f"{_.text} [DRT]")
            dic[__]={'value':f' {_.text} [DRT]', 'bgcolor':'#5d5dd9', 'color':'#fff'}
            count_ents+=True 
        elif word in list_categ_ents_c2[3]: 
            message_ents.append(f"{_.text} [WEP]")
            dic[__]={'value':f' {_.text} [WEP]', 'bgcolor':'#E74C3C', 'color':'#fff'}
            count_ents+=True 
        elif word in list_categ_ents_c2[4]: 
            message_ents.append(f"{_.text} [UNT]")
            dic[__]={'value':f' {_.text} [UNT]', 'bgcolor':'#3498DB', 'color':'#fff'}
            count_ents+=True 
        elif word in list_categ_ents_c2[5]: 
            message_ents.append(f"{_.text} [VHC]")
            dic[__]={'value':f' {_.text} [VHC] ','bgcolor':'#9B59B6','color':'#fff',}
            count_ents+=True
        elif word in list_categ_ents_c2[6]: 
            message_ents.append(f"{_.text} [PLC]")
            dic[__]={'value':f' {_.text} [PLC]', 'bgcolor':'#1ABC9C', 'color':'#fff'}
            count_ents+=True
        else: 
            message_ents.append(f"{_.text}")
            dic[__]={'value':f'{_.text}', 'bgcolor':'rgba(255, 255, 255, .0)', 'color':'rgb(5, 242, 250)'}

    return message_ents, dic, count_ents

#...
def recognize_make_message_with_ents(*args):
    list_message_ents, message_with_ents = args[0], ''

    for _ in range(0, len(list_message_ents)): 
        message_with_ents += list_message_ents[_]+' '    
    message_with_ents = str(message_with_ents).replace(" .",".").replace(" ,",",")\
    .replace(" ?","?").replace(" !","!")#.replace('" ','"').replace(' "','"')

    return message_with_ents