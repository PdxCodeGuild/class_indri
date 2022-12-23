from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    form = TodoForm()

    context = {'todo': todo, 'form': form}


    return render(request, 'todo/index.html', context)

def save_todo(request):
    form = TodoForm(request.POST)
   
    if form.is_valid():
        todo = Todo()
        todo.save()

    return redirect('home')
    
    

