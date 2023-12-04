from django.urls import path
from .views import HomeView, MovieListView, AboutView, ContactView, SeatLayoutView, SaveContactView

app_name = 'MTB'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('movies/seat-layout/', SeatLayoutView.as_view(), name='seat_layout'),
    path('movies/seat-layout/contact/savedata/', SaveContactView.as_view(), name='save_contact')
]

