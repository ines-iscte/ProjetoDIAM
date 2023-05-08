from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
]