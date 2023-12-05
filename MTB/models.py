from django.db import models
from datetime import datetime

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()  # in minutes, you can adjust as needed
    image = models.URLField(blank=True, null=True)  # allows blank values and accepts URLs

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    payment = models.CharField(max_length=100)
    cardnumber = models.IntegerField(max_length=16, default=None)
    cardexpirydate = models.CharField(max_length=7, default=datetime.now().strftime('%m/%Y'))

class UpcomingMovie(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    link = models.URLField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.name

