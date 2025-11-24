from django.urls import path
from django.contrib.auth import views as auth_views
from api import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register()

app_name = 'api'

urlpatterns = [   
    path('messages/', views.get_messages, name="get_messages"),
    path('rooms/', views.get_rooms, name="get_rooms"),
    path('get_recognize_entity/', views.get_recognize_entity),
    path('post_recognize_entity/', views.post_recognize_entity),
    path('api_recognize_entity_by_post/<str:arg>/', views.api_recognize_entity_by_post),
    path('api_classify_priority_by_post', views.api_classify_priority_by_post),
    path('api_delivery_message_by_post', views.api_delivery_message_by_post),
    path('api_generate_statistic_by_post', views.api_generate_statistic_by_post),
]