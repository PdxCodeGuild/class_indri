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

"""Explanation:
The index function serves as the main page of the Django app. It does the following:
 - Retrieves all ShortenedURL objects from the database and orders them by the counter field in descending order. The ShortenedURL.objects.all() method retrieves all ShortenedURL objects from the database, and the .order_by('-counter') method sorts them by the counter field in descending order.
 - Creates a new URLForm object. The URLForm class is a Django form that allows the user to input a URL to be shortened.
 - Renders the 'shortener/index.html' template, passing in the list of ShortenedURL objects and the URLForm object as context. The render function takes in the request object, the name of the template to be rendered, and a dictionary of context data. The context data is made available to the template and can be used to populate the template with dynamic content.

The index function is called when the user navigates to the main page of the Django app. When the function is called, it retrieves all ShortenedURL objects from the database, creates a new URLForm object, and renders the 'shortener/index.html' template with the ShortenedURL objects and URLForm object as context. The rendered template is then returned as the response object and sent to the client.
"""


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

"""Explanation:
The save_url function does the following:
 - Creates a new URLForm object using the POST data from the request. The URLForm class is a Django form that allows the user to input a URL to be shortened. The URLForm object is created using the request.POST data, which contains the form submission data.
 - If the form is valid (i.e. all required fields are filled out and the data is in the correct format), the function creates a new ShortenedURL object, sets the url field to the URL entered in the form, generates a random 6-character code using ascii letters and digits, and saves the ShortenedURL object to the database.
 - Regardless of whether the form is valid or not, the function redirects the user back to the index page using the redirect function. The redirect function sends a redirect response to the client, telling the client to navigate to the specified URL. In this case, the URL is the index page of the Django app (which is specified using the 'index' URL pattern).

The save_url function is called when the user submits the form for creating a new shortened URL. When the function is called, it processes the form submission, creates a new ShortenedURL object if the form is valid, and redirects the user back to the index page.
"""

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

"""Explanation:
The relocate function does the following:
 - Retrieves all ShortenedURL objects from the database that have the given code. The ShortenedURL.objects.filter(code=code) method retrieves all ShortenedURL objects from the database that have a code field that matches the given code.
 - If at least one ShortenedURL object was found, the function gets the first ShortenedURL object (since we only expect there to be one), increments the counter field by 1, saves the updated ShortenedURL object to the database, and redirects the user to the original URL using the redirect function.
 - If no ShortenedURL object was found, the function redirects the user back to the index page using the redirect function.

The relocate function is called when the user navigates to a shortened URL using the unique code. When the function is called, it retrieves the ShortenedURL object from the database that corresponds to the given code, increments the counter field, and redirects the user to the original URL.
"""