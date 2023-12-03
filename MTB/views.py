# MTB/views.py

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Movie  # Import your Movie model

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class MovieListView(View):
    def get(self, request):
        return render(request, 'movie.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class SeatLayoutView(View):
    def get(self, request):
        return render(request, 'seatlayout.html')
