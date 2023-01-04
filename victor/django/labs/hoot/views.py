from django.shortcuts import render, redirect
from .models import Hoot
from .forms import HootForm
from django.contrib.auth.decorators import login_required
def home(request):
    posts = Hoot.objects.all().order_by('-created_date')
    return render(request, 'hoot/index.html', {'posts': posts})

@login_required
def create(request):
    if request.method == 'GET':
        form = HootForm()
    else:
        form = HootForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['hoot']
            public = form.cleaned_data['public']
            new_post = Hoot()
            new_post.title = title
            new_post.hoot = body
            new_post.public = public
            new_post.user = request.user
            new_post.save()
            return redirect('profile')

    return render(request, 'hoot/create.html', {'form': form})

    




