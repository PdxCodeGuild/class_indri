from django.shortcuts import render, redirect
from .models import Post
from .forms import NewPost
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    posts = Post.objects.all().order_by('-date_created')
    context = {
        "posts":posts
    }
    return render(request, 'posts/index.html', context)

@login_required
def compose(request):
    
    if request.method == "GET":
        form = NewPost()
        
    else:
        
        form = NewPost(request.POST)
        
        if form.is_valid():
            body = form.cleaned_data['body']
            public = form.cleaned_data['public']
            
            new_post = Post()
            new_post.user = request.user
            new_post.body = body
            new_post.public = public
            new_post.save()
            
            return redirect('profile')
            
            
    return render(request, 'posts/compose.html', {"form":form})