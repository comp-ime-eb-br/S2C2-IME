import json
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message
from core.views import make_processing_recognize_entity, api_generate_statistic_by_post
from nltk.tokenize import word_tokenize
import time as tm
from library.views import debug_statment
from statistic.views import *
from datetime import time

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data             = json.loads(text_data)
        message          = data['message']
        username         = data['username']
        room             = data['room']
        photo            = data['photo']
        recognize_entity = data['nlp']
        priority         = False
        message_raw      = message

        # print("-"*72,"\n\n\n")
        # print(data['photo'])
        # print("\n\n\n","-"*72)

        start_time = tm.time()

        if recognize_entity: 
            content  = make_processing_recognize_entity(data['message'])#['message_with_ents']#[4]#(4)
            message  = content['message_with_ents']
            priority = content['message_priority']

        #print(' >> consumers : priority : ',priority,'\n\n')

        end_time = tm.time()
        duration = f'{end_time - start_time:4f} sec'

        await self.save_message(username, room, message, priority, duration)

        #===> debug_statment("processing time : ",duration)

        #... Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'duration': duration,
                'priority': priority,
                'photo': photo,
                'message_raw':message_raw
            }
        )

    #... Receive message from room group
    async def chat_message(self, event):
        message  = event['message']
        username = event['username']
        duration = event['duration']
        priority = event['priority']
        photo    = event['photo']
        message_raw = event['message_raw']

        #... Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message' : message,
            'username': username,
            'duration': duration,
            'priority': priority,
            'photo':photo
        }))

        #... Mosafi. after send the message to websocket the model call api generate statistic
        #api_generate_statistic_by_post(message_raw)
        statistic_make_statistic_message(message_raw)

    @sync_to_async
    def save_message(self, username, room, message, priority, duration):
        _user = User.objects.get(username=username)
        _room = Room.objects.get(slug=room)
        _priority = priority
        _duration = duration

        Message.objects.create(user=_user,room=_room,content=message,priority=_priority,duration=_duration)
        
