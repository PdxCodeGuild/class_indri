from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_letters, digits, punctuation, ascii_lowercase, ascii_uppercase
from .helpers import unit_converter as uc # renaming unit_converter to uc because we already have a unit_converter function in this file

# Create your views here.
def index(request):
    return render(request, 'lab1_redo/index.html')


def password_generator(request):
    if request.method == "GET":
        return render(request, 'lab1_redo/password_gen.html')
    else:
        form = request.POST
        error = ""
        length = 0
        try:
            length = int(form['user_input'])
        except ValueError:
            error = "Invalid input"

        characters = ascii_letters + digits + punctuation
        password = random.choices(characters, k=length)

        password = "".join(password)

        return render(request, 'lab1_redo/password_gen.html', {'password': password, 'error': error})


def rot(request):
    return render(request, 'lab1_redo/rot_cypher.html')

def rotate(request):

    message = request.POST['message']
    rotation_amount = 13
    alphabet = ascii_letters

    output = ""
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            position = (position + rotation_amount) % len(alphabet)
            output += alphabet[position]

    return render(request, 'lab1_redo/rot_cypher.html', {"output": output})



def unit_converter(request):
    if request.method == "GET":
        return render(request, 'lab1_redo/unit_converter.html')
    else:
        distance = float(request.POST['distance'])
        unit = request.POST['unit']
        result = uc(distance, unit)
        return render(request, 'lab1_redo/unit_converter.html', {'result': result})

history = []
results = {
    "wins": 0,
    "losses": 0
}


def rps(request):
    context = {
        "history": history,
        "wins": results['wins'],
        "losses": results['losses']
    }
    return render(request, 'lab1_redo/rps.html', context)


def rps_game(request, user_choice):

    choices = ["rock", "paper", "scissors"]

    cpu = random.choice(choices)

    if user_choice not in choices:
        history.append("Invalid choice.")
    elif user_choice == cpu:
        history.append("You tied.")
    elif (user_choice == "paper" and cpu == "scissors") or (user_choice == "rock" and cpu == "paper") or (user_choice == "scissors" and cpu == "rock"):
        history.append("You lost.")
        results['losses'] += 1
    else:
        history.append("You win!")
        results['wins'] += 1

    context = {
        "history": history,
        "wins": results['wins'],
        "losses": results['losses']
    }

    return render(request, 'lab1_redo/rps.html', context)