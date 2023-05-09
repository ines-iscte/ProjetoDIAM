from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
]

urlpatterns = [
    path('login/', views.log_in, name="log_in"),
]