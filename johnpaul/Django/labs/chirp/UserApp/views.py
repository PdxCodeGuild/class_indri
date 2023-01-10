from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from  . forms import SignUpForm, BaseForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout




# register view
def register(request):
  if request.method == 'GET':
    form = SignUpForm()
  else:
    form = SignUpForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      password_confirmation = form.cleaned_data['password_confirmation']

      if password == password_confirmation:
        user = User()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password)
        user.save()
        return redirect('login')
  return render(request, 'UserApp/register.html', {'form': form})




# login view
def login(request):
  if request.method == 'GET':
    form = BaseForm()
  else:
    form = BaseForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        user_login(request, user)
        return redirect('home')
      else:
        return redirect('login')
  return render(request, 'UserApp/login.html', {'form': form})


#logout view
def logout(request):
  user_logout(request)
  return render(request, 'UserApp/logout.html')


# profile view
@login_required
def profile(request):
  return render(request, 'UserApp/profile.html')

#create post
def new_post(request):
  return render(request, 'UserApp/post_home.html')
