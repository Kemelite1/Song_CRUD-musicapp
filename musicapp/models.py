from django.db import models
class Artiste(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    age = models.PositiveSmallIntegerField()
      
      
    def __str__(self):
        return self.first_name


class Song(models.Model):
    artise_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, null=False)
    likes = models.PositiveIntegerField()
    release = models.DateTimeField()


    def __str__(self):
        return self.title

class  Lyrics(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, null=False)
    content = models.TextField()