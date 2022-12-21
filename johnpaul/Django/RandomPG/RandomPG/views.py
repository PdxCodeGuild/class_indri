from django.shortcuts import render, redirect
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
            return render(request, 'RandomPG/home.html',{'password': password, 'form': form})
        else:
            return render(request, 'RandomPG/home.html', {'form': form})


    else:
        form = InputForm()
        return render(request, 'RandomPG/home.html', {'form': form})
       


def rps(request):
    return render(request, 'RandomPG/rps.html')

outcome = ""
def rps_game(request, user_choice):
    choices = ['rock', 'paper', 'scissors']
    cpu = random.choice(choices)
    if user_choice not in choices:
        outcome = "".join('Invalid choice.')
    elif user_choice == cpu:
        outcome = "".join('Game tied')
    elif (user_choice == 'rock' and cpu == 'paper') or (user_choice == 'paper' and cpu == 'scissor') or (user_choice == 'scissors' and cpu == 'rock'):
        outcome = "".join('You lost!')
    else:
        outcome = "".join('You win!')
    
    return render(request, 'RandomPG/rps.html', {'outcome': outcome})
        


