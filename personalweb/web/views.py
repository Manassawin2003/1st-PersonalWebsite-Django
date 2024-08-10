from django.shortcuts import render
from .models import Profile

def home(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'web/home.html', context)


