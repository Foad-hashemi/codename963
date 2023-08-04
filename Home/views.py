from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View,TemplateView
from Tracks.models import *
from .sessions import Recent


class Home(View):

    def get(self, request, play_context=None):
        tracks = Track.objects.order_by('-released_time')
        albums = Album.objects.all()
        topalbum = Album.objects.get(views__gte=400)
        genre = Genre.objects.all()
        recent = request.session.get('Recently').values()
        recent_list = []
        for track in recent:
            recent_list.append(Track.objects.get(slug=track['track_name']))
        return render(request, 'Home/home.html', {'tracks': tracks[0:15], 'albums': albums[0:6], 'topalbum': topalbum,
                                                   'recent': recent_list, 'genres': genre[0:7],'play':play_context})



class AddRecent(View):
    def get(self, request):
        track_name = request.GET.get('name')
        track_artist = request.GET.get('artist')
        session = Recent(request)
        session.add(slug=track_name,artist=track_artist)
        play_context = Track.objects.get(slug=track_name)
        main = Home()
        return main.get(request=request,play_context=play_context)


def index(request):
    paginator= Paginator(Track.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj": page_obj}
    return render(request, "Home/index.html", context)