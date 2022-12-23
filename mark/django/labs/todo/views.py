from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import user_input

# Create your views here.

def index(request):
    all_todos = TodoItem.objects.all()
    
    form = user_input()
    
    return render(request, 'todo/index.html', {"all_todos":all_todos, "form":form})

def save_todo(request):
    
    form = user_input(request.POST)
    
    if form.is_valid():
        todo_item = TodoItem()
        todo_item.entry = form.cleaned_data['input']
        todo_item.save()
    
    print(request.POST)

    return redirect('index')