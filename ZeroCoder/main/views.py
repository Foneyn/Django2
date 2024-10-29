from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home_view(request):
    return render(request, 'main/home.html')


def about_view(request):
    return render(request, 'main/about.html')


def contact_view(request):
    return render(request, 'main/contact.html')


def services_view(request):
    return render(request, 'main/services.html')