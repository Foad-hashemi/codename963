from django.db import models
# from django.forms.models import ValidationError
# def FileVlidation(filename):
#     if '.mp3' not in filename:
#         raise ValidationError('wrong format')


class Genre(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='tracks/genres')
    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=60, unique=True)
    artist = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tracks/albums')
    released_Time = models.DateField()
    album = models.ManyToManyField(Genre, related_name='albums')
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60)
    artist = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tracks/image')
    file = models.FileField(upload_to='tracks/tracks',)
    released_time = models.DateField()
    duration = models.FloatField()

    def __str__(self):
        return f'{self.name}--{self.album}'
