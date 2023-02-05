from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Chirp
from .forms import ChirpForm


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = ChirpForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                chirp = form.save(commit=False)
                chirp.user =request.user
                chirp.save()
                messages.success(request, ("Your Chirp Was Posted!"))
                return redirect('home')


        chirps = Chirp.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"chirps":chirps, "form":form})
    else:
        chirps = Chirp.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"chirps":chirps})
    

def profile_list(request):
    return render(request, 'profile_list.html')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        chirps = Chirp.objects.filter(user_id=pk)

        return render(request, "profile.html", {"profile":profile, "chirps":chirps})
    else:
        messages.success(request, ("You Must be Logged In"))
        return redirect('home')
    
    