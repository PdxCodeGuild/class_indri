from django.shortcuts import render
from .forms import UserSignUpForm

# Create your views here.
def signup(request):
  form = UserSignUpForm
  return render(request, 'users_app/signup.html', {'form': form})
