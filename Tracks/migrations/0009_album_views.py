# Generated by Django 4.2.3 on 2023-07-31 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0008_track_released_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
