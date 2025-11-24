from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.core_home, name='core_home'),
    path('get/', views.get_message, name='get_message'),
    path('post/', views.post_message, name='post_message'),
    path('get_post_recognize/', views.get_post_recognize),
]
