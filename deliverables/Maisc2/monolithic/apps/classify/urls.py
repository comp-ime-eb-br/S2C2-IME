from django.urls import path 
from django.contrib.auth import views as auth_views 
from recognize import views

app_name = 'classify' 

urlpatterns = [
    path('', views.classify_home, name='classify_home'),
]