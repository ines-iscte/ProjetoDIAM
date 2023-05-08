from django.shortcuts import render

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

