from django.shortcuts import render
from .forms import InputForm
import random
from string import ascii_letters, digits, punctuation


def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():         
            password_length = form.cleaned_data['password_length']
            character = ascii_letters + digits + punctuation
            password = random.choices(character, k=password_length)
            password = ''.join(password)
            return render(request, 'RandomPG/home.html', {'password': password})
    else:
        form = InputForm
        return render(request, 'RandomPG/home.html', {'form': form})
       

def about(request):
    return render(request, 'RandomPG/about.html', {'title': 'About'})
