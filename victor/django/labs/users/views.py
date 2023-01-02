from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import BaseForm as LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login as user_login, logout as user_logout


def login(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            user = authenticate(request, username=username_input, password=password_input)
            if user is not None:
                user_login(request, user)
                previous_page = request.GET.get('next')

                if previous_page is not None:
                    return redirect('profile')
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    user_logout(request)
    return redirect('login')

def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
    
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']

            if password == password_confirmation:
                user = User()
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
                return redirect('profile')

    return render(request, 'users/register.html', {'form': form})

    