from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm, BaseForm as LoginForm
from blog.models import BlogPost


# Login Function
def login(request):
    if request.method == "Get":
        form=LoginForm()
    else:
    # Create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            # Authenticate the user
            user = authenticate(
                request, username=username_input, password=password_input)
            # If user is found then log them in
            if user is not None:
                user_login(request, user)
                # If the user was trying to access a page before logging in
                # then redirect them to that page
                previous_page = request.GET.get('next')
                # If previous_page is not None then redirect to that page
                if previous_page is not None:
                    return redirect(previous_page)
                # If previous_page is None then redirect to the profile page
                else:
                    return redirect('profile')

    return render(request, "usersapp/login.html", {"form": form})
# Logout function
def logout(request):
    user_logout(request)
    # User will be redirected back to the login page after logining out
    return redirect('login')


def register(request):
    # If this is a GET request then create the default form
    if request.method == "GET":
        form = RegistrationForm()

    # If this is a POST request then process the Form data
    else:
        # Create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  # password123
            password_confirmation = form.cleaned_data['password_confirmation']

            # Check if the passwords match
            if password == password_confirmation:
                # Create a new user
                user = User()
                user.username = username
                user.email = email
                # Do not store the plain text password on the user model.
                # user.password = password
                # use .set_password() instead to store the hashed password to the db
                user.set_password(password)
                user.save()
                return redirect('profile')

    return render(request, 'usersapp/register.html', {'form': form})


@login_required
def profile(request):
    # Get all blogposts by user from db
    posts = BlogPost.objects.filter(
        user=request.user).order_by('-created_date')
    # Put all posts into context
    context = {
        "posts": posts
    }
    # Pass context into template
    return render(request, 'users/profile.html', context)