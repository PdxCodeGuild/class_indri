from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.utils import timezone

# Create your views here.
def index(request):
    todo = Todo.objects.filter(completed_date=None)
    todones = Todo.objects.exclude(completed_date=None)
    form = TodoForm()


    context = {'todo': todo, 'form': form, 'todones': todones}


    return render(request, 'todo/index.html', context)

def save_todo(request):
    form = TodoForm(request.POST)
   
    if form.is_valid():
        todo = Todo()
        todo.text = form.cleaned_data['todo']
        todo.save()

    return redirect('home')

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')

def complete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed_date = timezone.now()
    todo.save()
    print(todo.completed_date)
    print(timezone.now())
    return redirect('home')
   
    
    

