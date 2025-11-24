from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.core_home, name='core_home'),
    path('get_post_delivery/', views.get_post_delivery),
]