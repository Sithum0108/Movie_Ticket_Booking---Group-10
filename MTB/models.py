from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()  # in minutes, you can adjust as needed
    image = models.ImageField()  # assumes you have an 'images' folder in your media root

    def __str__(self):
        return self.title
