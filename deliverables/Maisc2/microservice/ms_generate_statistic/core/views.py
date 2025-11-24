# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import time
import requests 
from .serializers import StatisticSerializers
from .models import Statistic
from statistic.views import *

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
                'message':'I am the FIFTH container','container_name':'generate statistic',
                'bgcolor':'secondary',}       

    # BLOCK END
    #==================================================================     
    template = 'core/content/home/home.html'
    return render (request, template, context)

#------------------------------------------------------------------------
# 
#------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def get_post_statistic(request):

    #...
    _statistic = Statistic.objects.all()
    _serializers = StatisticSerializers(_statistic, many=True)
    
    #...
    if request.method == 'POST':
        
        start_time = time.time()
        _data = request.data
        serializer = StatisticSerializers(data =_data)

        if serializer.is_valid():
            _message_raw = _data['message_input']

            #...
            _host_sender, _ip_sender, _host_receiver, _ip_receiver, _noun_count, _verb_count,\
            _pron_count, _adje_count, _punc_count, _num_count, _adve_count, _conj_count, _det_count, \
            _other_count,_lst_noun,_lst_verb,_lst_adve,_lst_pron,_lst_adje, _lst_punc, _lst_conj, \
            _lst_det, _lst_num, _lst_other = make_generate_statistic(_message_raw)

            # print("-"*72,"\n\n\n")
            # print(" >> STATISTIC : ", _message_raw)
            # print("\n\n\n","-"*72)

            end_time = time.time()
            duration = f'{end_time - start_time:4f} sec'

            serializer.validated_data['message_input']  = _message_raw      # 0
            serializer.validated_data['duration']       = duration  
            serializer.validated_data['host_sender']    = _host_sender
            serializer.validated_data['ip_sender']      = _ip_sender
            serializer.validated_data['host_receiver']  = _host_receiver
            serializer.validated_data['ip_receiver']    = _ip_receiver
            serializer.validated_data['noun_count']     = _noun_count 
            serializer.validated_data['verb_count']     = _verb_count 
            serializer.validated_data['pron_count']     = _pron_count 
            serializer.validated_data['adje_count']     = _adje_count
            serializer.validated_data['punc_count']     = _punc_count
            serializer.validated_data['num_count']      = _num_count 
            serializer.validated_data['adve_count']     = _adve_count
            serializer.validated_data['conj_count']     = _conj_count
            serializer.validated_data['det_count']      = _det_count 
            serializer.validated_data['other_count']    = _other_count
            serializer.validated_data['lst_noun']       = _lst_noun
            serializer.validated_data['lst_verb']       = _lst_verb
            serializer.validated_data['lst_adve']       = _lst_adve
            serializer.validated_data['lst_pron']       = _lst_pron
            serializer.validated_data['lst_adje']       = _lst_adje
            serializer.validated_data['lst_punc']       = _lst_punc
            serializer.validated_data['lst_conj']       = _lst_conj
            serializer.validated_data['lst_det']        = _lst_det
            serializer.validated_data['lst_num']        = _lst_num
            serializer.validated_data['lst_other']      = _lst_other 

            serializer.save()

            # print("-"*72,"\n\n\n")
            # print(" >> DELIVERY AFTER SAVE   : ", serializer.data)
            # print("\n\n\n","-"*72)

            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else: print(" >> none method was activated....")

    return Response(_serializers.data)