from rest_framework import serializers
from django.contrib.auth.models import User
from room.models import Message, Room

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message 
        fields = ["content","room","user"] #'__all__'

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"