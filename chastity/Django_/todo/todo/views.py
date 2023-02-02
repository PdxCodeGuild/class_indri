from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

# Create your views here.

def index(request):
    tasks =TodoItem.objects.all()
    form = TodoItemForm()

    context = {'tasks':tasks, 'form':form}
    return render(request, 'todo/index.html', context)


def save_tasks(request):
    form = TodoItemForm(request.POST)
   
    if form.is_valid():
        tasks= TodoItem()
        tasks.text = form.cleaned_data['input']
        tasks.save()

    return redirect('index')
    
def remove_tasks(request, id):
    tasks = TodoItem.objects.get(id=id)
    tasks.delete()
   
    return redirect('index')

def finished_tasks(id):
    tasks = TodoItem.objects.get(id=id)
    tasks.save()
    
    return redirect('index')