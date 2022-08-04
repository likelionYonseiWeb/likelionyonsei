from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def alumni(request):
    return render(request, 'alumni.html')

def recruit(request):
    return render(request, 'recruit.html')

def contact(request):
    return render(request, 'contact.html')