# views is request handler, request -> response, action
from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_letters, digits, punctuation

def index(request):
    return render (request, 'rock_paper_lab/base.html')

def password_generator(request): 
    if request.method=="GET":
        return render(request, 'rock_paper_lab/password_gen.html')
    else:
        form = request.POST
        length = 0
        try: 
            length =int(form['user_input'])
        except ValueError:
            error = "Invalid input"
        characters=ascii_letters+ digits + punctuation
        password=random.choices(characters, k=length)
        password="".join(password)

        return render(request, 'rock_paper_lab/password_gen.html', {'Password': password })


# Rock Paper Function

score_history = []
results = {
    "wins": 0,
    "losses": 0
}

def rocks_paper_score(request):
    context = {
        "history": score_history,
        "wins": results['wins'],
        "losses": results['losses']
    }
    return render(request, 'rock_paper_lab/rock_paper_game.html', context)

def game_function(request, user_pick): 
    choices = ["rock", "paper", "scissors"]

    ai = random.choice(choices)
 
    if user_pick not in choices:
        score_history.append("Invalid choice.")
    elif user_pick == ai:
        score_history.append("You tied.")
    elif (user_pick == "paper" and ai == "scissors") or (user_pick == "rock" and ai == "paper") or (user_pick == "scissors" and ai == "rock"):
        score_history.append("You lost.")
        results['losses'] += 1
    else:
        score_history.append("You win!")
        results['wins'] += 1

    context = {
        "history": score_history,
        "wins": results['wins'],
        "losses": results['losses']
    }

    return render(request, 'rock_paper_lab/rock_paper_game.html', context)

