from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()  # in minutes, you can adjust as needed
    image = models.URLField(blank=True, null=True)  # allows blank values and accepts URLs

    def __str__(self):
        return self.title
