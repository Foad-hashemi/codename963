# Generated by Django 4.2.3 on 2023-07-31 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0007_album_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='released_time',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
