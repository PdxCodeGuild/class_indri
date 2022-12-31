from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def compose(request):
    return render(request, 'home/compose.html')

def edit(request):
    return render(request, "home/edit.html")