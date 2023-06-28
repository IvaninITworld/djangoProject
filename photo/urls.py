from django.urls import path
from django.views.generic import ListView, DetailView

from photo.models import Album, Photo

app_name = 'photo'
urlpatterns = [
    path('', ListView.as_view(model=Album), name='index'),
    path('album', ListView.as_view(model=Album), name='album_list'),
    path('album/<int:pk>/', DetailView.as_view(model=Album), name='album_detail'),
    path('photo/<int:pk>/', DetailView.as_view(model=Photo), name='photo_detail'),
]
