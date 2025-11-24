# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializers, RoomSerializers
from room.models import Message, Room
import requests
import json
from unicodedata2 import normalize
import unicodedata


#...
@api_view(['GET', 'POST'])
def get_rooms(request):
    _rooms = Room.objects.all()
    _serializers = RoomSerializers(_rooms, many=True)
    return Response(_serializers.data)    


#...
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def get_messages(request):   
    _messages = Message.objects.all()
    _serializers = MessageSerializers(_messages, many=True)

    if request.method == 'GET': 
        print("  >> Método GET foi acionado....")
    #...
    elif request.method=='POST':
        _data = request.data

        #...
        serializer = MessageSerializers(data = _data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response(serializer.errors)
    else: 
        pass

    return Response(_serializers.data)


#...
def get_recognize_entity(request):
    
    url = 'http://192.168.91.62:8002/core/get_recognize/'
    response = requests.get(url)
    data = response.json()

    return JsonResponse(data[4]['message_output'], safe=False)


#...
def post_recognize_entity(request):
    
    url = 'http://192.168.91.62:8002/core/get_post_recognize/'

    json_data = {
        "message_input": "A coluna de tanques avançou pela estrada principal, demonstrando seu poderio militar."
    }

    request_type = 'POST'
    response = requests.request(request_type, url, data=json_data)
    data_return =  unicodedata.normalize('NFKD', json.dumps(response.text)).encode('ascii', 'ignore').decode('ascii')
    #unicodedata2.normailize('NFKD', json.dumps(response.text)).encode('ascii','ignore').decode('ascii')
    data_return = str(data_return).replace("\\","").replace(' ""','').replace('."','.')\
    .replace('"/','').replace("\\","").replace('"',"").replace('"','')

    return JsonResponse(data_return, safe=False)


#... api to recognize entities at container recognize entity
def api_recognize_entity_by_post(*args):
    
    url = 'http://192.168.91.65:8002/core/get_post_recognize/'

    json_data = {
        "message_input": str(args[0])
    }

    request_type = 'POST'

    # print("-"*72,"\n\n\n")
    # print(" ENTITY RECONGNITION MODULE DONE 111111...") #print(" >> ", json_load['message_tokens'], json_load['len_tokens'], json_load['lst_ents_posi'])
    # print("\n\n\n","-"*72)

    data_return = requests.request(request_type, url, data=json_data).text

    json_load = json.loads(data_return)

    # print("-"*72,"\n\n\n")
    # print(" ENTITY RECONGNITION MODULE DONE 222222...") #print(" >> ", json_load['message_tokens'], json_load['len_tokens'], json_load['lst_ents_posi'])
    # print("\n\n\n","-"*72)

    return json_load['message_tokens'], json_load['len_tokens'], json_load['lst_ents_posi'],\
    json_load['lst_ents_text'], json_load['lst_ents_kind'], json_load['list_message_ents'],\
    json_load['dict_message_ents'], json_load['count_ents'], json_load['message_output']


#... api to recognize entities at container recognize entity
def api_classify_priority_by_post(*args):

    url = 'http://192.168.91.69:8003/core/get_post_classify/'

    json_data = {
        "message_input"  : str(args[0]),
        "count_ents"     : str(args[1]),
        "message_tokens" : str(args[2])
    }

    request_type = 'POST'
    data_return = requests.request(request_type, url, data=json_data).text

    json_load = json.loads(data_return)

    # print("-"*72,"\n\n\n")
    # print(" PRIORITY CLASSIFICATION MODULE DONE...")
    # print("\n\n\n","-"*72)

    return json_load['priority'] #, json_load['sentiment'], json_load['len_sent'], json_load['lst_sent']


#... api to recognize entities at container recognize entity
def api_delivery_message_by_post(*args):

    url = 'http://192.168.91.70:8004/core/get_post_delivery/'

    json_data = {
        "message_input"  : str(args[0])
    }

    request_type = 'POST'
    data_return = requests.request(request_type, url, data=json_data).text

    json_load = json.loads(data_return)

    # print("-"*72,"\n\n\n")
    # print(" DELIVERY MESSAGE MODULE DONE...") #print(" >> ", json_load['message_tokens'], json_load['len_tokens'], json_load['lst_ents_posi'])
    # print("\n\n\n","-"*72)

    return json_load['background_message'], json_load['color_border_message'],\
    json_load['weight_border_message'], json_load['highlight_text_message']


#... 
def api_generate_statistic_by_post(*args):

    url = 'http://192.168.91.71:8005/core/get_post_statistic/'

    json_data = {
        "message_input"  : str(args[0])
    }

    request_type = 'POST'
    data_return = requests.request(request_type, url, data=json_data).text

    # print("-"*72,"\n\n\n")
    # print(" STATISTIC GENERATE MODULE DONE...") #print(" >> ", json_load['message_tokens'], json_load['len_tokens'], json_load['lst_ents_posi'])
    # print("\n\n\n","-"*72)

    json_load = json.loads(data_return)

    return json_load['host_sender'], json_load['ip_sender'],json_load['host_receiver'],\
    json_load['ip_receiver'],json_load['noun_count'],json_load['verb_count'],\
    json_load['pron_count'], json_load['adje_count'],json_load['punc_count'],\
    json_load['num_count'],json_load['adve_count'],json_load['conj_count'],\
    json_load['det_count'],json_load['other_count'], json_load['lst_noun'], \
    json_load['lst_verb'], json_load['lst_adve'],json_load['lst_pron'], \
    json_load['lst_adje'], json_load['lst_punc'],json_load['lst_conj'], \
    json_load['lst_det'], json_load['lst_num'],json_load['lst_other']