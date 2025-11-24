from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'

urlpatterns = [   
    path('', views.account_login, name='account_login'),
    path('logout/', views.account_logout, name='account_logout'),
    path('register/', views.account_register, name='account_register'),
    path('edit/', views.account_edit, name='account_edit'),       
]