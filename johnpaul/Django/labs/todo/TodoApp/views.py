from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import TodoItem
from django.views.generic.edit import CreateView, UpdateView


def TodoApp(request):
  uncompleted_todo_item = TodoItem.objects.all().order_by('-created_date')
  return render(request, 'TodoApp/index.html', {'uncompleted_todo_item': uncompleted_todo_item})


#USING CRUD operations: Create, Retrive, Update, Delete
class TodoCreateView(CreateView):
  form_class = TodoForm
  template_name = 'todo_create.html'
  success_url = '/home/'
  
 
  

class TodoUpdateView(UpdateView):
    pass



 

  
# class TodoDeleteView(DeleteView):
#   model = TodoItem
#   fields = ['text', 'created_date', 'date_due']




