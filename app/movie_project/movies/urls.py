from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('movies/', views.MovieList.as_view(), name="add_movie"),
]
