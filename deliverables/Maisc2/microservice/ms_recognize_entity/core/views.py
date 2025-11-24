# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from recognize.views import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import time
import requests 
from .serializers import RecognizeSerializers
from .models import Recognize


@api_view(['GET', 'POST'])
def get_post_recognize(request):
    #...
    _recognize = Recognize.objects.all()
    _serializers = RecognizeSerializers(_recognize, many=True)

    #...
    if request.method == 'GET': 
        print("  >> Método GET foi acionado....")

    elif request.method == 'POST':
        start_time = time.time()
        _data = request.data
        serializer = RecognizeSerializers(data =_data)

        if serializer.is_valid():
            message_raw = serializer.validated_data['message_input']

            message_tokens, len_tokens, lst_ents_posi, lst_ents_text, lst_ents_kind, list_message_ents, \
            dict_message_ents, count_ents, message_with_ents = recognize_get_entity_message(message_raw)

            end_time = time.time()
            duration = f'{end_time - start_time:4f} sec'

            serializer.validated_data['message_tokens']     = message_tokens    #0
            serializer.validated_data['len_tokens']         = len_tokens        #1
            serializer.validated_data['lst_ents_posi']      = lst_ents_posi     #2
            serializer.validated_data['lst_ents_text']      = lst_ents_text     #3
            serializer.validated_data['lst_ents_kind']      = lst_ents_kind     #4
            serializer.validated_data['list_message_ents']  = list_message_ents #5
            serializer.validated_data['dict_message_ents']  = dict_message_ents #6
            serializer.validated_data['count_ents']         = count_ents        #7               
            serializer.validated_data['message_output']     = message_with_ents #8
            serializer.validated_data['duration']           = str(duration)     #9

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)
    
    else: print(" >> none method was activated....")

    return Response(_serializers.data)

#...
@api_view(['GET','POST'])
def post_message(request):
    url = 'http://192.168.91.62:8001/api/messages/'
    json_data = {
        "content": "Abvun the bash maia 1, teteiimalcutar",
        "room": 1,
        "user": 1
    }
    request_type = 'POST'
    response = requests.request(request_type, url, data=json_data)
    return JsonResponse(response, safe=False)

#...
def get_message(request):
    url = 'http://192.168.91.62:8001/api/messages/'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data, safe=False)

#...
def core_home(request):
    # BLOCK START
    #==================================================================  
    template = context = None 
    section, title_page, title_sheet = 'core', 'Project', 'Project'
    container_name, message_title = 'container recognize entites', 'I am the SECOND container'

    # BLOCK CENTER
    #================================================================== 
    message_tokens, len_tokens, lst_ents_posi, lst_ents_text, lst_ents_kind, \
    list_message_ents,  dict_message_ents, count_ents, message_with_ents = \
    recognize_get_entity_message('O soldado jurou defender seu país até o último suspiro.')

    # BLOCK END
    #==================================================================      
    context  = {'section':section,'title_page':title_page,'title_sheet':title_sheet,
                'message_title':message_title,'container_name':container_name,
                'bgcolor':'primary', 'message_with_ents': message_with_ents}       
    template = 'core/content/home/home.html'
    return render (request, template, context)


