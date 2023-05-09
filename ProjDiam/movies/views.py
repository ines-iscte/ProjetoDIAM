from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Movie

app_name = 'movies'

def index (request):
    return HttpResponse("Seja bem vindo à nossa aplicação!")

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movielist.html', {'movies': movies})


def search_movies(request):
    query = request.GET.get('query', '')
    movies = Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {'movies': movies, 'query': query}
    return render(request, 'search_results.html', context)

