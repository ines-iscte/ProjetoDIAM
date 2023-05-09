from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Movie

app_name = 'movies'

def index (request):
    return HttpResponse("Seja bem vindo à nossa aplicação!")

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movielist.html', {'movies': movies})

def addMovie(request):
    return render(request, 'movies/addMovie.html')

def registerMovie(request):
    if request.method == 'POST':
        new_movie = Movie(title=request.POST['title'], year=request.POST['year'], description=request.POST['description'], duration=request.POST['duration'], genre=request.POST['genre'], rating=request.POST['rating'], photo=request.POST['photo'])
        new_movie.save()
        return HttpResponseRedirect(reverse('movies'))
    else:
        if request.user.is_superuser:
            return render(request, 'movies/addMovie.html')
        else:
            return HttpResponseRedirect(reverse('movies'))

