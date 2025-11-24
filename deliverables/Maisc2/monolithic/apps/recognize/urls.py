from django.urls import path 
from django.contrib.auth import views as auth_views 
from recognize import views

app_name = 'recognize' 

urlpatterns = [
    path('', views.recognize_home, name='recognize_home'),
]
