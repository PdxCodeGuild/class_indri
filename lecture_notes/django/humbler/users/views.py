from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm


# login
def login(request):
    return HttpResponse("This is the login page.")


# logout
def logout(request):
    return HttpResponse("This is the logout page.")


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
                user.set_password(password)
                user.save()
                return redirect('profile')

    return render(request, 'users/register.html', {'form': form})


# profile
def profile(request):
    return HttpResponse("This is the profile page.")
