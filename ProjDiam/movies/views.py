from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

app_name = 'movies'

def index (request):
    return HttpResponse("Seja bem vindo à nossa aplicação!")

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movielist.html', {'movies': movies})

def log_in(request):
    if request.method == 'POST':
        # handle form data
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # log in user and redirect to home page
            login(request, user)
            return redirect('movie_list')
        else:
            # display error message
            messages.error(request, 'Invalid username or password.')
        # if request method is GET or authentication failed, display login page
    return render(request, 'login.html')