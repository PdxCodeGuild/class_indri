from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm


def TodoApp(request):
  uncompleted_todo_item = TodoItem.objects.all()
  return render(request, 'TodoApp/index.html', {'uncompleted_todo_item': uncompleted_todo_item})

def SaveToDoItem(request):
  form = TodoForm(request.POST)
  print((request.POST))
  if form.is_valid():
    save_todo_item = TodoItem()
    save_todo_item = form.cleaned_data('text')
    save_todo_item.save()
  return redirect('home')
