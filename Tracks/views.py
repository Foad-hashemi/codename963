from django.shortcuts import render
from .models import Track, Genre , Album
from django.views.generic import ListView


class AlbumsList(ListView):
    template_name = 'album.html'
    queryset = Album.objects.order_by('released_Time')
    context_object_name = 'albums'






