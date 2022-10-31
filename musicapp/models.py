 from turtle import title
from django.db import models
from datetime import datetime


class Artiste(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 400)
    age = models.IntegerField(max_length = 20)

class Song(models.Model):
    Artiste-models.ForeignKey(Artiste, on_delete = models.PROTECT)
    title = models.CharField(max_length = 100)
    date_released = models.DateTimeField(max_length = 50)
    likes = models.CharField(max_length = 120);
    Artiste_id = models.CharField(max_length = 100)
    
class Lyrics(models.Model):
    Song-models.ForeignKey(Song, on_delete = models.PROTECT)
    content = models.CharField(max_length = 100)
    song_id = models.CharField(max_length = 100)
