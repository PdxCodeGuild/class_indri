from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

# Create your views here.
def signup(request):
    
    if request.method == "GET":
        form = SignUpForm()
        
    else:
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            
            if password == password_confirm:
                
                user = User()
                user.username = email
                user.email = email
                user.set_password = password
                user.save()
                return redirect('profile')    
    
    
    return render(request, "users/signup.html", {'form':form})

def login(request):
    
    if request.method == "GET":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            
            user = authenticate(
                request, username=username_input, password=password_input)
            
            if user is not None:
                user_login(request, user)
                return redirect('profile')
            
            
    return render(request, "users/login.html", {'form':form})


def profile(request):
    return render(request, "users/profile.html")