from django.urls import path
from . import views


app_name = 'Home'

urlpatterns = [
    path('', views.Home.as_view(), name='Main'),
    path('play', views.AddRecent.as_view(), name='add'),
    path('test', views.index, name='a')
]
