from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from posts.models import Post

# ----------------------------------------------
#  Sign up for Yodel
def signup(request):
    
    if request.method == "GET":
        form = SignUpForm()
        
    else:
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            
            if password == password_confirm:
                
                user = User()
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
                user_login(request, user)
                return redirect('profile')    
    
    
    return render(request, "users/signup.html", {'form':form})

# ----------------------------------------------
# Log in to an existing account

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

# ----------------------------------------------
# log out of account
def logout(request):
    user_logout(request)
    return redirect('login')

# ----------------------------------------------
# return the profile page
@login_required
def profile(request):
    
    posts = Post.objects.filter(
        user=request.user)
    
    context = {
        "posts":posts,
    }
    
    return render(request, "users/profile.html", context)

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('profile')