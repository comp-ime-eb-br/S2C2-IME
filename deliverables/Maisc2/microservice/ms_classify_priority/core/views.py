# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import time
import requests 
from .serializers import ClassifySerializers
from .models import Classify
from classify.views import *

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
def core_home(request):
    
    # BLOCK START
    #==================================================================  
    template = context = None 
    section, title_page, title_sheet = 'core', 'Project', 'Project'
        
    # BLOCK CENTER
    #================================================================== 
    context  = {'section':section,'title_page':title_page,'title_sheet':title_sheet,
                'message':'I am the THIRD container','container_name':'classify priority',
                'bgcolor':'danger',}       

    # BLOCK END
    #==================================================================       
    template = 'core/content/home/home.html'
    return render (request, template, context)


#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def get_post_classify(request):
    #...
    _classify = Classify.objects.all()
    _serializers = ClassifySerializers(_classify, many=True)
    
    #...
    if request.method == 'POST':
        
        start_time = time.time()
        _data = request.data
        serializer = ClassifySerializers(data =_data)

        if serializer.is_valid():
            _message_raw = _data['message_input']
            _count_ents  = _data['count_ents']
            _message_tokens = _data['message_tokens']

            # print("-"*72,"\n\n\n")
            # print(" >> CLASSIFY MESSAGE : ", _message_raw)
            # print(" >> CLASSIFY ENTS NUM : ", _count_ents)
            # print(" >> CLASSIFY TOKENS : ", _message_tokens)
            # print("\n\n\n","-"*72)

            message_priority = classify_make_priority_message(_message_raw, _count_ents, _message_tokens)

            # print("-"*72,"\n\n\n")
            # print(" >> CLASSIFY MESSAGE_RAW : ", _message_raw)
            # print("\n\n\n","-"*72)

            end_time = time.time()
            duration = f'{end_time - start_time:4f} sec'

            serializer.validated_data['message_input'] = _message_raw       # 0
            serializer.validated_data['priority']      = message_priority  # 1
            serializer.validated_data['sentiment']     = None #message_sentiment # 2
            serializer.validated_data['len_sentence']  = None #len_sent          # 3
            serializer.validated_data['lst_sentence']  = None #lst_sent          # 4
            serializer.validated_data['duration']      = duration          # 5

            serializer.save()

            # print("-"*72,"\n\n\n")
            # print(" >> CLASSIFY AFTER SAVE   : ", serializer.data)
            # print("\n\n\n","-"*72)

            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else: print(" >> none method was activated....")

    return Response(_serializers.data)