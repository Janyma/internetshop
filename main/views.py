from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Product

def product(request):
   products=Product.objects.all()
   #context ={'title': 'Titel', 'description': 'Description', 'price': 'Price'}
   return render(request, 'main/home.html', {'products':products})
def home(request):
  return HttpResponse('<h1> Main menu</h1>')
def about(request):
    return render(request, 'main/about.html', {'title': 'About shop'})
