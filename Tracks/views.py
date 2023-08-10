from django.shortcuts import render, redirect
from .models import Track, Genre, Album
from django.views.generic import ListView, View
from Home.sessions import Recent


class AlbumsList(ListView):
    template_name = 'Tracks/album.html'
    queryset = Album.objects.order_by('released_Time').distinct()
    context_object_name = 'albums'

class SingleAlbum(View):
    def get(self, request):
        if request.GET.get('name'):
            album_name = request.GET.get('name')
            album = Album.objects.get(name=album_name)
            genre = album.genre.get(name=request.GET.get('genre'))
            if request.GET.get('play') is not None:
                play = Track.objects.get(slug=request.GET.get('play'))
                session = Recent(request)
                session.add(slug=request.GET.get('play'))
                return render(request, 'Tracks/album_single.html',
                              {"tracks": album.track_set.all, "album": album, "genre": genre, "play": play})
            else:
                return render(request, 'Tracks/album_single.html',
                              {"tracks": album.track_set.all, "album": album, "genre": genre})

        else:
            return redirect('/')
