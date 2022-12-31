from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from  . forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



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
      date_of_birth = form.cleaned_data['date_of_birth']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      password_confirmation = form.cleaned_data['password_confirmation']

      if password == password_confirmation:
        user = User()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.date_of_birth = date_of_birth
        user.email = email
        user.set_password(password)
        user.save()
        return redirect('home')
  return render(request, 'UserApp/register.html', {'form': form})




# login view
def login(request):
  return render(request, 'UserApp/login.html')





# profile view


