from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View, TemplateView
from Tracks.models import *
from .sessions import Recent


class Home(View):

    def get(self, request, ):

        tracks = Track.objects.order_by('-released_time')
        albums = Album.objects.all()
        topalbum = Album.objects.get(views__gte=400)
        genre = Genre.objects.all()
        recent_list = []
        try:
            recent = request.session.get('Recently').values()
            for track in recent:
                recent_list.append(Track.objects.get(slug=track['track_name']))
        except:
            pass

        return render(request, 'Home/home.html', {'tracks': tracks[0:15], 'albums': albums[0:6], 'topalbum': topalbum,
                                                  'recent': recent_list, 'genres': genre[0:6]})
