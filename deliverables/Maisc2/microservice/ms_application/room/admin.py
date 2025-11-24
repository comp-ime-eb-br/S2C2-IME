from django.contrib import admin
from .models import Room, Message, Grupo, Hierarchy
from datetime import datetime
from django.utils.timezone import make_aware

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['room', 'user', 'content', 'duration', 'created']
    list_filter  = ['room']

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ['group',]

@admin.register(Hierarchy)
class HierarchyAdmin(admin.ModelAdmin):
    list_display = ['user', 'parent', 'child','room','created']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'slug', 'nlp', 'get_user', 'created']

    def get_user(self, obj):
        return [user.username for user in obj.user.all()]

