from django.shortcuts import render, redirect
from .models import ShortenedURL
from .forms import URLForm
import random
import string

def index(request):
    """
    Displays a list of all shortened URLs, as well as a form for creating new ones.
    """
    # Retrieve all ShortenedURL objects from the database and order them by counter in descending order
    all_urls = ShortenedURL.objects.all().order_by('-counter')

    # Create a new URLForm object
    form = URLForm()

    # Render the 'shortener/index.html' template, passing in the list of ShortenedURL objects and the URLForm object as context
    return render(request, 'shortener/index.html', {"objects": all_urls, "form": form})

def save_url(request):
    """
    Processes the form submission for creating a new shortened URL.
    """
    # Create a new URLForm object using the POST data from the request
    form = URLForm(request.POST)

    # If the form is valid (i.e. all required fields are filled out and the data is in the correct format)
    if form.is_valid():
        # Create a new ShortenedURL object
        shortened_url = ShortenedURL()
        # Set the 'url' field to the URL entered in the form
        shortened_url.url = form.cleaned_data['url']
        # Generate a random 6-character code using ascii letters and digits
        shortened_url.code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        # Save the ShortenedURL object to the database
        shortened_url.save()

    # Redirect the user back to the index page
    return redirect('index')

def relocate(request, code):
    """
    Redirects the user to the original URL corresponding to the given code.
    """
    # Retrieve all ShortenedURL objects from the database that have the given code
    urls = ShortenedURL.objects.filter(code=code)

    # If at least one ShortenedURL object was found
    if len(urls) > 0:
        # Get the first ShortenedURL object (since we only expect there to be one)
        url = urls[0]
        # Increment the counter by 1
        url.counter += 1
        # Save the updated ShortenedURL object to the database
        url.save()
        # Redirect the user to the original URL
        return redirect(url.url)

    # If no ShortenedURL object was found, redirect the user back to the index page
    return redirect('index')