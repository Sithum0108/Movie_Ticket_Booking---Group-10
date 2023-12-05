from django.contrib import admin
from .models import Movie, ContactInfo

admin.site.register(Movie)
admin.site.register(ContactInfo)
admin.site.register(UpcomingMovie)
admin.site.register(Feedback)
