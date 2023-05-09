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
  
def log_in(request):
    if request.method == 'POST':
        # handle form data
        username = request.POST['username']
        password = request.POST['password']
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

