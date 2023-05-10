from django.urls import path, include
from . import views

app_name= 'movies'
urlpatterns = [
    path("", views.log_in, name="log_in"),
    path('search/', views.search_movies, name='search_movies'),
    path("add_movie", views.add_movie, name="add_movie"),
    path("register_movie", views.register_movie, name="register_movie"),
    path('<int:movie_id>/detalhes', views.detail_movie, name='detail_movie'),
    path("movie_list", views.movie_list, name="movie_list"),
]


    
