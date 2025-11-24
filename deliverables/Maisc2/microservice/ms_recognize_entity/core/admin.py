from django.contrib import admin
from .models import Recognize

@admin.register(Recognize)
class RecognizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_input', 'message_output', 'message_tokens', 'duration', 'created']