from django.urls import path
from .views import *

app_name = 'Tracks'

urlpatterns = [
    path('albumlist', AlbumsList.as_view(), name='album_list'),
    path('album', SingleAlbum.as_view(), name='album')
]
