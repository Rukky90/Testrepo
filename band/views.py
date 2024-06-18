from django.shortcuts import render, redirect
from .models import Album
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    """
     Renders the home page.

     :param request(HttpRequest): The Http request object
     :returns:
          HttpResponse: rendered the home page.
          """
    return render(request, 'band/home.html')

def about(request):
    """
      Renders the about page

      :param request(HttpRquest):The HTTP request object
      :returns: 
          HttpResponse: The rendered about page 
    """
    return render(request, 'band/about.html')

def discography(request):
    """
    Renders the discography page with a list of all albums.

      :param
        request(HttpRequest): The HTTP request object.mro

        Returns:
            HttpResponse: The rendered discography page with a list of the albums.
    """
    album = Album.objects.all()
    return render(request, 'band/discography.html', {'album':album})


