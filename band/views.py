from django.shortcuts import render, redirect
from .models import Album
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'band/home.html')

def about(request):
    return render(request, 'band/about.html')

def discography(request):
    album = Album.objects.all()
    return render(request, 'band/discography.html', {'album':album})


