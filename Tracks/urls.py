from django.urls import path
from .views import AlbumsList

app_name = 'Tracks'

urlpatterns = [
    path('albums', AlbumsList.as_view(), name='album')
]
