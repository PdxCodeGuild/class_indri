from django.shortcuts import render,redirect
from .models import TodoItem
from .forms import ToDoForm
from django.utils import timezone

# Create your views here.
def index(request):
    todo_form = ToDoForm()
    todos = TodoItem.objects.all()
    return render (request, 'anthonytodo/index.html', {"form": todo_form, "todos_list": todos})
def make_list(request):
    # Create a new URLForm object using the POST data from the request
    form = ToDoForm(request.POST)

    # If the form is valid (i.e. all required fields are filled out and the data is in the correct format)
    if form.is_valid():
        # Create a new ShortenedURL object
        To_Do_Items = TodoItem()
        # Set the 'url' field to the URL entered in the form
        To_Do_Items.text = form.cleaned_data['to_do']
        # Generate
        To_Do_Items.created_date = timezone.now()
        # Save the To_Do_Items object to the database
        To_Do_Items.save()

    # Redirect the user back to the index page
    return redirect('/todo')

