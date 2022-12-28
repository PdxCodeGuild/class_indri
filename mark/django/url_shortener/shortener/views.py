from django.shortcuts import render, redirect
from .models import ShortenedURL
from .forms import URLForm
import random
import string



# Create your views here.
def index(request):
    
    all_urls = ShortenedURL.objects.all().order_by('-counter')
    
    form = URLForm()
    
    return render(request, 'shortener/index.html', {'objects': all_urls, "form":form})

def save_url(request):
    
    form = URLForm(request.POST)
    
    if form.is_valid():
        shortened_url = ShortenedURL()
        shortened_url.url = form.cleaned_data['url']
        shortened_url.code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        shortened_url.save()

    return redirect('index')
    
def relocate(request, code):
    
    urls = ShortenedURL.objects.filter(code=code)
    
    if len(urls) > 0:
        url = urls[0]
        url.counter += 1
        url.save()
        return redirect(url.url)
    
    return redirect('')