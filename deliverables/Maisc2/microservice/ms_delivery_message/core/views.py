# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import time
import requests 
from .serializers import DeliverySerializers
from .models import Delivery
from delivery.views import *

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
                'message':'I am the FOURTH container','container_name':'delivery message',
                'bgcolor':'success',}       

    # BLOCK END
    #==================================================================       
    template = 'core/content/home/home.html'
    return render (request, template, context)

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def get_post_delivery(request):
    #...
    _delivery = Delivery.objects.all()
    _serializers = DeliverySerializers(_delivery, many=True)
    
    #...
    if request.method == 'POST':
        
        start_time = time.time()
        _data = request.data
        serializer = DeliverySerializers(data =_data)

        if serializer.is_valid():
            _message_raw = _data['message_input']
 
            _background, _color, _weight, _highlight = make_delivery_message(_message_raw)

            # print("-"*72,"\n\n\n")
            # print(" >> delivery MESSAGE_RAW : ", _message_raw)
            # print("\n\n\n","-"*72)

            end_time = time.time()
            duration = f'{end_time - start_time:4f} sec'

            serializer.validated_data['message_input']          = _message_raw      # 0
            serializer.validated_data['background_message']     = _background 
            serializer.validated_data['color_border_message']   = _color 
            serializer.validated_data['weight_border_message']  = _weight 
            serializer.validated_data['highlight_text_message'] = _highlight 
            serializer.validated_data['duration']               = duration          # 5

            serializer.save()

            # print("-"*72,"\n\n\n")
            # print(" >> DELIVERY AFTER SAVE   : ", serializer.data)
            # print("\n\n\n","-"*72)

            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else: print(" >> none method was activated....")

    return Response(_serializers.data)