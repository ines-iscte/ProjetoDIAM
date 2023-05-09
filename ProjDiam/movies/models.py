from django.db import models

class Movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)
    duration = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    photo = models.FileField(upload_to='imagesMovies/', default="")


    def __str__(self):
        return self.title

    def getPhoto(self):
        return self.photo