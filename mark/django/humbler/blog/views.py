from django.shortcuts import render, redirect, get_object_or_404
from users.models import BlogPost
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required

def index(request):
    posts = BlogPost.objects.all().order_by('-date_created')
    return render(request, 'blog/index.html', {"posts":posts})

@login_required
def create(request):
    if request.method == "GET":
        form = NewPostForm()
    else: 
        form = NewPostForm(request.POST)
        if form.is_valid:
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            public = form.cleaned_data['public']
                
            new_post = BlogPost()
            new_post.title = title
            new_post.body = body
            new_post.public = public
            new_post.user = request.user
            new_post.save()
            
            return redirect('profile')
            
    return render(request, 'blog/create.html', {"form":form})

@login_required
def edit(request, blog_id):
    
    blog = get_object_or_404(BlogPost, id=blog_id, user=request.user)
    
    
    if request.method == "GET":
        form = NewPostForm({
            'title': blog.title,
            'body': blog.body,
            'public': blog.public,
        })
    else:
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            public = form.cleaned_data['public']
            
            blog.title = title
            blog.body = body
            blog.public = public
            blog.save()
            
            return redirect('profile')
            
        
    
    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'blog/edit.html', context)