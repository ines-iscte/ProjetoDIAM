from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.urls import reverse
from django.core.checks import messages
from .models import Movie

app_name = 'movies'

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def search_movies(request):
    query = request.GET.get('query', '')
    movies = Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(genre__icontains=query))
    context = {'movies': movies, 'query': query}
    return render(request, 'movies/search_movie.html', context)

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
            return HttpResponseRedirect(reverse('movies:movie_list'))
        else:
            # display error message
            messages.error(request, 'Invalid username or password.')
        # if request method is GET or authentication failed, display login page
        return render(request, 'movies/login.html')
    else:
        return render(request, 'movies/login.html')

def add_movie(request):
    return render(request, 'movies/add_movie.html')

def register_movie(request):
    if request.method == 'POST':
        new_movie = Movie(title=request.POST['title'], year=request.POST['year'], description=request.POST['description'], duration=request.POST['duration'], genre=request.POST['genre'], rating=request.POST['rating'], photo=request.FILES.get('photo'))
        new_movie.save()
        return HttpResponseRedirect(reverse('movies:movie_list'))
    else:
        if request.user.is_superuser:
            return render(request, 'movies/add_movie.html')
        else:
            return HttpResponseRedirect(reverse('movies:movie_list'))

def detail_movie(request, movie_id):
    movies = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movies}
    return render(request, 'movies/detail_movie.html', context)
