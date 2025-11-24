from django.shortcuts import render
from django.core.files import File
from pathlib import Path
import re
import json
from datetime import datetime
import numpy as np
from time import process_time
import os
from library.views import *

#...
def make_generate_statistic(*args):
    _noun_count, _verb_count, _pron_count, _adje_count, _punc_count, _num_count, _adve_count, \
    _conj_count, _det_count, _other_count = get_count_grammar_message(args[0])
    _lst_noun, _lst_verb, _lst_adve, _lst_pron, _lst_adje, _lst_punc, _lst_conj, _lst_det, \
    _lst_num, _lst_other = make_list_with_grammar_message(args[0])
    _host_sender, _ip_sender  = get_host_and_ip_sender()    
    _host_receiver, _ip_receiver = get_host_and_ip_receiver() 

    return _host_sender, _ip_sender, _host_receiver, _ip_receiver, _noun_count, _verb_count,\
    _pron_count, _adje_count, _punc_count, _num_count, _adve_count, _conj_count, _det_count, \
    _other_count,_lst_noun,_lst_verb,_lst_adve,_lst_pron,_lst_adje, _lst_punc, _lst_conj, \
    _lst_det, _lst_num, _lst_other

#... 
def statistic_make_dictionary_message(args):
    message_json = {
        'message':{
            'main':{
                'message_raw':args['message_raw'],
                'message_with_ents':args['message_with_ents'],
            },
            'properties':{
                'tokens':args['message_tokens'],
                'date':args['date'], 
                'tokens_len':args['len_tokens'],
                'host_sender':args['host_sender'], 
                'host_receiver':args['host_receiver'], 
                'ip_sender': args['ip_sender'], 
                'ip_receiver':args['ip_receiver'],
                'start_processing':args['start_processing'],
                'finish_processing':args['finish_processing'], 
                'time_processing':args['time_processing'],
            },
            'priority':{
                'status':args['message_priority'],
            },
            'entities':{
                'ents_posi':args['lst_ents_posi'],
                'ents_text':args['lst_ents_text'],
                'ents_kind':args['lst_ents_kind']
            },
            'sentence':{
                'len_sent':args['len_sent'],
                'lst_sent':str(args['lst_sent'])
            },
            'grammar':{
                'count':{
                    'tot_noun' :str(args['noun_count']),'tot_verb' :str(args['verb_count']),
                    'tot_pron' :str(args['pron_count']),'tot_adej' :str(args['adje_count']),
                    'tot_punc' :str(args['punc_count']),'tot_adve' :str(args['adve_count']),
                    'tot_conj' :str(args['conj_count']),'tot_det'  :str(args['det_count']),
                    'tot_num'  :str(args['num_count']),'tot_other':str(args['other_count'])
                },
                'concept':{
                    'lst_noun':args['lst_noun'],'lst_verb':args['lst_verb'],'lst_adve':args['lst_adve'],
                    'lst_pron':args['lst_pron'],'lst_adje':args['lst_adje'],'lst_punc':args['lst_punc'],
                    'lst_conj':args['lst_conj'],'lst_det':args['lst_det'],'lst_num':args['lst_num'],
                    'lst_other':args['lst_other']
                },
            }
        }
    }

    # message_json = json.dumps(api_maisc2)
    save_message_json(message_json)

    return message_json


#---------------------------------------------------
#
#---------------------------------------------------
def save_message_json(*args):
    message = args[0]
    with open("static/download/data_message_json.json", "w") as write_file:        
        json.dump(message, write_file, indent=4, sort_keys=True)

    return True
