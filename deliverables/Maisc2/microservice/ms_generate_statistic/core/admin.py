from django.contrib import admin
from .models import Statistic

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_input', 'duration', 'created']
