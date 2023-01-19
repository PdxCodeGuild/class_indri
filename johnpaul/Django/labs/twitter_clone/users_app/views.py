from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required





def signup(request):
  if request.method == 'GET':
    form = UserSignUpForm()
  else:
    form = UserSignUpForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      password_confirmation = form.cleaned_data['password_confirmation']
      if password == password_confirmation:
        user = User()
        user.email = email()
        user.username = username()
        user.set_password(password)
        user.save()
        return redirect('profile')
  return render(request, 'users_app/signup.html', {'form': form})

@login_required
def user_profile(request):
  return render (request, 'users/profile.html')


