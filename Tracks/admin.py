from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Genre)
admin.site.register(models.Album)


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'album']
    prepopulated_fields = {'slug': ['name']}
