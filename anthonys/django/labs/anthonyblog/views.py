# from django.shortcuts import render
# from .models import BlogData
# # Create your views here.
# from django.shortcuts import render,redirect

# # Create your views here.
# def blogs(request):
#     blogs= BlogData.object.all.order_by('created_date')
#     return render (request, 'anthonyblog/base.html', {'blogs': blogs})

# -------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogData
from .forms import NewBlogForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# Index view - show all public posts
def index(request):
    # Get all public posts and order by date created (newest first)
    blogs = BlogData.objects.all().order_by('-created_date')
    return render(request, 'anthonyblog/index.html', {'blogs': blogs})


# Create view - create a new post (only for logged in users)
@login_required
def create(request):
    # If this is a GET request then create the default form
    if request.method == "GET":
        form = NewBlogForm()
    # If this is a POST request then process the Form data
    else:
        # Create a form instance and populate it with data from the request:
        form = NewBlogForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            public = form.cleaned_data['public']

            # Create a new blog post object and save to the database
            new_post = BlogData()
            new_post.title = title
            new_post.body = body
            new_post.public = public
            new_post.user = request.user
            new_post.save()

            # Once finished redirect to the profile page
            return redirect('profile')

    # If this is a GET (or any other method) render the default form
    return render(request, 'anthonyblog/create.html', {"form": form})


# Edit view - edit an existing post (only for logged in users)
@login_required
def edit(request, blog_id):

    # Search for blog with given id and is current user, return 404 if not found
    blog = get_object_or_404(BlogData, id=blog_id, user=request.user)

    # If this is a GET request then create a form with current blog data
    if request.method == "GET":
        form = NewBlogForm({
            'title': blog.title,
            'body': blog.body,
            'public': blog.public
        })
    # If this is a POST request then process the Form data
    else:
        form = NewBlogForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            public = form.cleaned_data['public']

            # Update the blog post object and save to the database
            blog.title = title
            blog.body = body
            blog.public = public
            blog.save()

            # Once finished redirect to the profile page
            return redirect('profile')

    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'anthonyblog/edit.html', context)