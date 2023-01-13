from django.shortcuts import render
import random
from  string import ascii_letters, digits, punctuation

# Create your views here.
def index(request):
    return render(request, 'lab_redo/index.html')


def password_generator(request):
    if request.method == "GET":
        return render(request, 'lab_redo/password_gen.html')
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

        password ="".join(password)
        print("PASSWORD", password)

        return render(request, 'lab_redo/password_gen.html', {'password': password, 'error': error})