from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.core_home, name='core_home'),
    path('message_login_required/', views.message_login_required, name='message_login_required'), 
    path('message_warning/', views.message_warning, name='message_warning'),   
]

