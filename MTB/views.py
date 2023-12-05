# MTB/views.py

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Movie, ContactInfo, Feedback 

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie.html', {'movies': movies})

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class SeatLayoutView(View):
    def get(self, request):
        return render(request, 'seatlayout.html')

def save_to_database(request):
    if request.method == 'GET':
        #data = request.GET.get('')   

        customer_name = request.GET.get('name')
        customer_email = request.GET.get('email')
        customer_phone = request.GET.get('phone')
        customer_payment = request.GET.get('payment')
        customer_card_number = request.GET.get('cardnumber')
        customer_card_expiry_date = request.GET.get('cardexpirydate')
        #customer_card_cvv = request.GET.get('cardcvv')

        ContactInfo_instance = ContactInfo(name=customer_name, email=customer_email, phone=customer_phone, payment=customer_payment, 
                                           cardnumber=customer_card_number, cardexpirydate=customer_card_expiry_date,
        )
        ContactInfo_instance.save()

        return JsonResponse({'message': 'Your seats are SUCCESSFULLY RESERVED'})  
    else:
        return JsonResponse({'error': 'Invalid request method'})   



def save_about_data(request):
    if request.method == 'GET': 

        commentor_name = request.GET.get('commentname')
        commentor_messege = request.GET.get('commentmessage')
        
        Feedback_instance = Feedback(name=commentor_name, comment=commentor_messege,
        )
        Feedback_instance.save()

        return JsonResponse({'message': 'Contact Information Added successfully'})  
    else:
        return JsonResponse({'error': 'Invalid request method'})   

    
