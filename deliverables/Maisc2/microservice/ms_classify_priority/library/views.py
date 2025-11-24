import unicodedata
from datetime import datetime
from django.contrib.auth.models import User
from library.categories import *
import unicodedata
from nltk.tokenize import TreebankWordTokenizer
from nltk.util import ngrams
import socket
from django.contrib.auth import logout
import socket
from datetime import datetime
import numpy as np
from time import process_time


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def library_main_start_processing(*args):

    _message_raw = str(args[0]).replace("'","")
    _start_processing = process_time()
    _datetime_now = datetime.now() 
    _date = str(_datetime_now.strftime("%d/%m/%Y"))

    return _message_raw, _start_processing, _date

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def library_main_finish_processing(_start_processing):

    _finish_processing = process_time()
    _time_processing = _finish_processing - _start_processing
    _time_processing = "{0:.5f}".format(_time_processing)
    _finish_processing = str(_finish_processing)
    _start_processing = str(_start_processing)

    return _finish_processing, _time_processing, _finish_processing, _start_processing


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def register_audit_user(user_current, section):
    user = user_current
    host = socket.gethostname()
    ip   = socket.gethostbyname(host)
    section = section

    instance = Audit(user=user,host=host,ip=ip,section=section)
    instance.save()

    account:logout()

    return True


#------------------------------------------------------------------------
#
#------------------------------------------------------------------------
def get_time_processing():
    datetime_now = datetime.now() 
    return str(datetime_now.strftime("%H:%M:%S:%f"))


#------------------------------------------------------------------------
#
#------------------------------------------------------------------------
def get_tokens_at_message(*args):
    token = TreebankWordTokenizer()
    message_tokens = token.tokenize(args[0])
    len_tokens = str(len(message_tokens))

    return message_tokens, len_tokens    


#------------------------------------------------------------------------
#
#------------------------------------------------------------------------
def get_host_and_ip_sender():
    host_sender = socket.gethostname()
    ip_sender   = socket.gethostbyname(host_sender)

    return host_sender, ip_sender


#------------------------------------------------------------------------
#
#------------------------------------------------------------------------
def get_host_and_ip_receiver():
    host_receiver = socket.gethostname()
    ip_receiver   = socket.gethostbyname(host_receiver)

    return host_receiver, ip_receiver


#------------------------------------------------------------------------
#
#------------------------------------------------------------------------
def get_sentence_message(*args):
    nlp = load_nlp()[1]
    lst_sent, doc = [], nlp(args[0])

    for sent in doc.sents:
        lst_sent.append(sent)
    len_sent = len(lst_sent)

    return len_sent, lst_sent


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def make_message_with_ents(*args):
    list_message_ents, message_with_ents = args[0], ''

    for _ in range(0, len(list_message_ents)): 
        if _=='.':message_with_ents += str(list_message_ents[_]).lstrip()+''
        else: message_with_ents += list_message_ents[_]+' '

    return message_with_ents


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def get_classify_priority_message(*args):
    message_raw, count_ents = args
    interrogation = '?'

    message_priority = True if count_ents > 2 or interrogation in message_raw else False

    return message_priority


#------------------------------------------------------------------------
# count grammar each word
#------------------------------------------------------------------------
def get_count_grammar_message(args):
    message_raw = args
    noun_count = verb_count = pron_count = adje_count = punc_count = 0
    adve_count = conj_count = det_count = num_count = other_count = 0

    #... load module spacy with raw message
    nlp_spacy = load_nlp()[1]
    doc_parsing = nlp_spacy(message_raw)    

    #... grammar countable
    for q in doc_parsing:            
        #... count grammar items message
        if q.pos_  == 'NOUN': noun_count+=True
        elif q.pos_== 'VERB': verb_count+=True
        elif q.pos_== 'PRON': pron_count+=True
        elif q.pos_== 'ADJ' : adje_count+=True
        elif q.pos_== 'PUNCT':punc_count+=True
        elif q.pos_== 'NUM' : num_count+=True
        elif q.pos_== 'ADV' : adve_count+=True
        elif q.pos_== 'CONJ': conj_count+=True 
        elif q.pos_== 'DET' : det_count+=True
        else: other_count+=True

    return noun_count, verb_count, pron_count, adje_count, punc_count, \
    num_count, adve_count, conj_count, det_count, other_count


#------------------------------------------------------------------------
# make list with ents properties
#------------------------------------------------------------------------
def make_list_with_properties_ents(*args):
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


#------------------------------------------------------------------------
# get entities at message and return a dictionary and a list with it 
#------------------------------------------------------------------------
def get_entities_c2_message(args):
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


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def get_sentiment_anlisys_message(*args): 
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
def get_acronym_kind_ents(args):
    kind_ents = None
    
    if args == 'ACTION': kind_ents = 'ACT'
    elif args == 'AGENT': kind_ents = 'AGT'
    elif args == 'VEHICLE': kind_ents = 'VHC'
    elif args == 'PLACE': kind_ents = 'PLC'
    elif args == 'WEAPONS': kind_ents = 'WEP'
    elif args == 'UNIT': kind_ents = 'UNT'
    elif args == 'DIRECTION': kind_ents = 'DRT'
    
    return kind_ents



#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def make_list_with_grammar_message(*args):
    lst_noun, lst_verb, lst_adve, lst_pron, lst_adje, lst_punc, lst_conj, \
    lst_det, lst_num, lst_other = [],[],[],[],[],[],[],[],[],[]

    nlp = load_nlp()[1]
    doc = nlp(args[0])

    for _ in doc:            
        if _.pos_  == 'NOUN': lst_noun.append(_.text)
        elif _.pos_== 'VERB': lst_verb.append(_.text)
        elif _.pos_== 'PRON': lst_pron.append(_.text)
        elif _.pos_== 'ADJ' : lst_adje.append(_.text)
        elif _.pos_== 'PUNCT':lst_punc.append(_.text)
        elif _.pos_== 'NUM' : lst_num.append(_.text)
        elif _.pos_== 'ADV' : lst_adve.append(_.text)
        elif _.pos_== 'CONJ': lst_conj.append(_.text)
        elif _.pos_== 'DET' : lst_det.append(_.text)
        else: lst_other.append(_.text)
    
    return lst_noun, lst_verb, lst_adve, lst_pron, lst_adje, lst_punc, \
           lst_conj, lst_det, lst_num, lst_other


#------------------------------------------------------------------------
# get current user
#------------------------------------------------------------------------
def get_user_current(user_):    
    try: 
        user_current = User.objects.get(username = user_)
    except User.DoesNotExist:
        user_current = None        

    return user_current


#------------------------------------------------------------------------
# remove all accent of the words
#------------------------------------------------------------------------
def remove_accent_word(args):
    return ''.join(ch for ch in unicodedata.normalize('NFKD', args) if not unicodedata.combining(ch))


#------------------------------------------------------------------------
# set lower case
#------------------------------------------------------------------------
def set_lower_case_word(args):
    return str(args).lower()


#------------------------------------------------------------------------
# set Upper case
#------------------------------------------------------------------------
def set_upper_case_word(args):
    return str(args).upper()


#---------------------------------------------
#
#---------------------------------------------
def remove_accent_word(text):           
    # BLOCK START
    #==================================================================
    text = str(text).lower()
    if text=='tiros'or text=='tiro':text='tiroteio'
     
    # BLOCK MIDDLE
    #==================================================================  
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")   
          
    # BLOCK END
    #==================================================================  
    return str(text)	

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def debug_statment(*args):

    print("--------------------------\n\n\n")
    print(f' >> {args[0]} : {args[1]}')
    print('\n\n\n---------------------------')

