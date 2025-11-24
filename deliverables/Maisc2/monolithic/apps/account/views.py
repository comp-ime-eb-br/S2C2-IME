from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from library.views import *
from django.db import connection
import random

def account_home(request):
    # BLOCK START
    #==================================================================   
    section, title_page, title_sheet = 'sendc2', 'Home', 'Home'

    # BLOCK END
    #================================================================== 
    context  = {'section':section, 'title_page':title_page,'title_sheet':title_sheet,}
    template = 'sendec2/home/home.html'
    return render(request, template, context)
             
                          
def account_login(request):
    # BLOCK START
    #==================================================================  
    form = cd = user = context = template = message_text = \
    message_color = user_current = None 
    section, title_page, title_sheet = 'sendc2', 'Login', 'Login'    
    
    # BLOCK MAIN
    #==================================================================  
    if request.method == 'POST':      
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])                
            if user is not None:                
                if user.is_active:
                    login(request, user)                                    
                    user_current = get_user_current(request.user)           
                    return redirect ('core:core_home')                             
                else:
                    return HttpResponse('Disabled account')
            else:
                message_text = 'Usuário ou senha inválida!'
                message_color = 'alert-danger'
    else:
        form = LoginForm()
                                     
    # BLOCK END
    #==================================================================        
    context  = {'form': form, 'section':section,'title_page':title_page,'title_sheet':title_sheet,
                'message_text':message_text,'message_color':message_color,'user_current':user_current,}
    template = 'sendc2/home/home.html'                       
    return render(request,template,context)


@login_required
def account_edit(request):
    # BLOCK START
    #==================================================================  
    context = template = message_text = message_color = user_current = None 
    section, title_page, title_sheet = 'sendc2', 'Plataforma', 'Maisc2'  
    list_color = ['primary', 'success', 'danger', 'info', 'warning']

     
    # BLOCK MAIN
    #==================================================================  
    user_current = get_user_current(request.user)
    color = random.choice(list_color)

    #... verify if current user to inner profile
    profile = Profile.objects.filter(user=request.user).exists()
    
    if not profile:
        user_current_id = user_current.id

        #... create new user at profile model
        con        = connection
        cursor     = con.cursor()
        SQLProfile = "INSERT INTO account_profile(user_id, collor) VALUES("+str(user_current_id)+", '"+str(color)+"')"
        cursor.execute(SQLProfile)
        con.commit()
                    
    #...    
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        
        #... verify if user and profile is validy
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            message_text = 'Seu perfil atualizado com sucesso!'
            message_color = 'alert-success'
            
        else:
            message_text = 'Ocorreu um erro na atualização do perfil!'
            message_color = 'alert-danger'
            
        context  = {'section':section,'title_page':title_page,'title_sheet':title_sheet,
                    'message_text':message_text,'message_color':message_color,
                    'user_current':user_current}
        template = 'sendc2/home/home.html'  
        return render(request,template,context)   
    
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)   
        
    # BLOCK END
    #================================================================== 
    context  = {'user_form': user_form,'profile_form': profile_form,}
    template = 'account/edit/edit.html'    
    return render(request, template, context)


def account_logout(request):
    # BLOCK START
    #==================================================================  
    form = cd = user = context = template = message_text = message_color = user_current = None 
    section, title_page, title_sheet = 'sendc2', 'Logout', 'Logout'    
    
    # BLOCK MAIN
    #==================================================================  
    message_text = f"{str(request.user).title()}, você foi desconectado com sucesso!"
    message_color = 'alert-warning'
    logout(request)
                    
    # BLOCK END
    #==================================================================        
    return redirect ('core:core_home')

    
def account_register(request, *args, **kwargs):
    # BLOCK START
    #==================================================================  
    form = user = context = template = message_text = message_color = None 
    section, title_page, title_sheet = 'sendc2', 'Register', 'Register'  
    
    # BLOCK MAIN
    #==================================================================  
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            #... Create the user profile
            Profile.objects.create(user=new_user)
            
            message_text   = 'Cadastrado com sucesso. '
            message_color  = 'alert-success'
            message_signup = 'Clique para entrar '
            
            context  = {'section':section,'title_page':title_page,'title_sheet':title_sheet,'message_text':message_text,
                        'message_color':message_color,'user':new_user,'message_signup':message_signup,}
            template = 'sendc2/content/home/home.html'  
            return render(request, template, context)            
        else:
            message_text = str(user_form.errors).replace("/","").replace("<li>","").replace("<ul>",""). \
                replace('<ul class="errorlist">username<ul class="errorlist">',"")
            message_color = 'alert-danger'
    else:
        user_form = UserRegistrationForm()    

    # BLOCK END
    #==================================================================        
    context  = {'form': form, 'section':section,'title_page':title_page,'title_sheet':title_sheet, 
                'message_text': message_text,'message_color':message_color, 'user':user,}
    template = 'core/sendc2/home.html'                       
    return render(request,template,context)

