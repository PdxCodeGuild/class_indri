from django.shortcuts import render
from .models import TodoItem
from .forms import ToDoForm

# Create your views here.
def index(request):
    return render (request, 'anthonytodo/index.html')
def make_list(request):
    # Create a new URLForm object using the POST data from the request
    form = ToDoForm(request.POST)

    # If the form is valid (i.e. all required fields are filled out and the data is in the correct format)
    if form.is_valid():
        # Create a new ShortenedURL object
        To_Do_Items = TodoItem()
        # Set the 'url' field to the URL entered in the form
        To_Do_Items.text = form.cleaned_data['text']
        # Generate a random 6-character code using ascii letters and digits
        To_Do_Items.created_date = DateField()
        # Save the To_Do_Items object to the database
        To_Do_Items.save()

    # Redirect the user back to the index page
    return redirect('index')



    return render (request, 'anthonytodo/todo.html')

