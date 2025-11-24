from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Message, Hierarchy
from library.views import get_user_current
import json
from nltk.tokenize import word_tokenize
from django.http import JsonResponse
from django.views.decorators.http import require_POST

#...
@login_required(login_url='core:message_login_required')
def rooms_home(request):
    # BLOCK START
    #==================================================================  
    section, title_page, title_sheet = 'chatc2', 'Chat C2', 'Chat C2'
    rooms = list_user_room = None

    # BLOCK MAIN
    #================================================================== 
    user_current = get_user_current(request.user.username)

    #...
    rooms = Room.objects.filter(user=user_current.id)
    list_user_room = [(s.user, list(s.user.all()),) for s in rooms]

    #...
    if len(rooms)<=1: return redirect('room:room_chat',rooms[0].slug)
    elif len(rooms)>1: return redirect('room:room_chat',rooms[0].slug)

    # BLOCK END
    #================================================================== 
    context = {'rooms':rooms,'user_current':user_current,'list_user_room':list_user_room, 
               'section':section, 'title_page':title_page, 'title_sheet':title_sheet}
    template = 'room/rooms_home.html'
    return render(request, template, context)

#...
@login_required(login_url='core:message_login_required')
def room_chat(request, slug):
    # BLOCK START
    #==================================================================  
    room = messages_room_first = hierarchy_user = user_current = room1 = room2 = None
    list_room_user, dict_room_user, section = [], {}, 'chatc2'
    section, title_page, title_sheet = 'chatc2', 'Chat C2', 'Chat C2'
    first_room, second_room, messages_room_second, room2_nlp = None, None, None, None
    background_message, color_border_message = 'alert alert-danger','border border-danger'
    weight_border_message,highlight_text_message = 'border-2', 'success'

    # BLOCK MAIN
    #================================================================== 
    user_current = get_user_current(request.user)
    user_photo   = user_current.profile.photo

    #...
    room  = Room.objects.get(slug=slug)
    rooms_user = Room.objects.filter(user=user_current)
    
    #...
    for _ in rooms_user:
        dict_room_user[_]={'room':_.room,'user':_.user}
        list_room_user.append(_.slug)

    #...
    if len(list_room_user)>1: 
        first_room, second_room = list_room_user[0], list_room_user[1]
        messages_room_first  = Message.objects.filter(room__slug=first_room).order_by('-id')[:72][::-1]
        messages_room_second = Message.objects.filter(room__slug=second_room).order_by('-id')[:72][::-1]
        room1 = Room.objects.get(slug=first_room)
        room1_nlp = room1.nlp
        room2 = Room.objects.get(slug=second_room)
        room2_nlp = room2.nlp
    else: 
        first_room = list_room_user[0]
        messages_room_first = Message.objects.filter(room__slug=slug).order_by('-id')[:72][::-1]
        room1 = Room.objects.get(slug=first_room)     
        room1_nlp = room1.nlp

    lst, dic = [], {}
    for __, _ in enumerate(messages_room_first):
        #print('>> ',_.content)
        token_msg = str(_.content).split(" ")
        lst.append(token_msg)

    for w in range(0, len(lst)):
        for count, q in enumerate(range(0, len(lst[w]))):
            color = '#FFFFFF'
            if lst[w][q]=='[ACT]': bgcolor = '#00FFFF'
            elif lst[w][q]=='[AGT]': bgcolor = '#F1C40F'
            elif lst[w][q]=='[DRT]': bgcolor = '#5d5dd9'
            elif lst[w][q]=='[VHC]': bgcolor = '#9B59B6'
            elif lst[w][q]=='[UNT]': bgcolor = '#3498DB'
            elif lst[w][q]=='[WEP]': bgcolor = '#E74C3C'
            elif lst[w][q]=='[PLC]': bgcolor = '#1ABC9C'
            else: 
                bgcolor = 'transparent'
                color = '#000000'
            dic[w,count] = {count:{'term':lst[w][q], 'bgcolor':bgcolor, 'color':color}}          
            #print(color)  
        break

    # BLOCK END
    #==================================================================     
    template = 'room/room_chat.html'
    context  = {'user_current':user_current,'room':room,'messages_room_first':messages_room_first,
                'messages_room_second':messages_room_second,'rooms_user':rooms_user,'hierarchy_user':
                hierarchy_user,'dict_room_user':dict_room_user,'section':section,'first_room':first_room,
                'second_room':second_room, 'title_page':title_page, 'title_sheet':title_sheet,
                'list_room_user':list_room_user,'user_photo':json.dumps(str(user_photo)),'hidden_scroll':True,
                'dic':dic, 'room1_nlp':room1_nlp,'room2_nlp':room2_nlp, 'background_message':background_message,
                'color_border_message':color_border_message,'weight_border_message':weight_border_message, 
                'highlight_text_message':highlight_text_message}    
    
    return render(request, template, context)

#...
def room_nlp(request, slug):
    if request.method == 'POST':
        nlp = request.POST.get('nlp')

        if nlp == 'true':
            nlp = True
        else:
            nlp = False
        room = Room.objects.get(slug=slug)
        room.nlp = nlp
        room.save()  # Save the changes to the task
        return JsonResponse({'status': 'success'})