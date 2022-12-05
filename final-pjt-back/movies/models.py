from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):

    title = models.CharField(max_length=50)
    popularity = models.FloatField()
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    release_date = models.DateField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()