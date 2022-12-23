# views is request handler, request -> response, action
from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_letters, digits, punctuation

def index(request):
    return render (request, 'rock_paper_lab/index.html')

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

# Create your views here.
