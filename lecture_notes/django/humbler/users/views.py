from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, BaseForm as LoginForm


# login
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
                previous_page = request.GET.get('next')
                if previous_page is not None:
                    return redirect(previous_page)
                else:
                    return redirect('profile')

    return render(request, "users/login.html", {"form": form})


# logout
def logout(request):
    user_logout(request)
    return redirect('login')


# register/signup
def register(request):
    if request.method == "GET":
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  # password123
            password_confirmation = form.cleaned_data['password_confirmation']

            if password == password_confirmation:
                user = User()
                user.username = username
                user.email = email
                # Do not store the plain text password on the user model.
                # user.password = password
                user.set_password(password)
                user.save()
                return redirect('profile')

    return render(request, 'users/register.html', {'form': form})


# profile
@login_required
def profile(request):
    return render(request, 'users/profile.html')
