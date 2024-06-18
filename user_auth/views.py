from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm

# Create your views here.
def user_login(request):
    """
      Renders the login page 
      
      :Param request: HttpRequest object 
      :return: HttpResponse object rendering the login template.
    """

    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
     Authenticate a user and logs them in if the credential are valid

     :param request: HttpRequest containing Post data with username and password.

     Returns:
      HttpResponseRedirect to show_user view  if authentication is successful.
      HttpResponseRedirect to user_login view if authentication fails 
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('user_auth:user_login')
        )
    else:
        login(request, user)
    return HttpResponseRedirect(
        reverse('user_auth:show_user')
    )

def show_user(request):
    """
     Displays the username of the logged-in user

     :param request: HttpRequest object.
     :returns:
         HttpResponse object rendering the user template with the username context.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username
    })

def register(request):
    """
    Renders the registration page

    :param request: Httprequest object.
    :returns:
          HttpResponse object rendering the registration template.
    """
    return render(request, 'authentication/register.html')

def signup(request):
    """
      Handles user signup process. If the request method is POST and the form is valid,
      saves the user and log them in. Otherwise render the signup form.

      :param request: HttpRequest object containing POST data with signup details.
      :returns: 
            HttpResponseRedirect ro band:home if signup is successful.
            httpResponseRedirect object rendering the registration template with the form.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('band:home')
    else:
        form = SignupForm()
    return render(request, 'authentication/register.html', {'form': form})