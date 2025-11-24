from django.urls import path 
from django.contrib.auth import views as auth_views 
from delivery import views

app_name = 'delivery' 

urlpatterns = [
    path('', views.delivery_home, name='delivery_home'),
]

