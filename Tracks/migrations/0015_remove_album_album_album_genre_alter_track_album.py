# Generated by Django 4.2.1 on 2023-08-04 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0014_alter_track_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='Tracks.genre'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracks.album'),
        ),
    ]
