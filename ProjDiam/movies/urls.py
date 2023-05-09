from django.urls import path, include
from . import views

app_name= 'movies'
urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("add_movie", views.addMovie, name="addMovie"),
    path("register_movie", views.registerMovie, name="registerMovie"),

]

urlpatterns = [
    path('login/', views.log_in, name="log_in"),
]