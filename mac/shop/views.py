from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("About Us")

def contact(request):
    return HttpResponse("Contact Us")

def tracker(request):
    return HttpResponse("Tracker Page")

def search(request):
    return HttpResponse("Search Page")

def productview(request):
    return HttpResponse("Product View")

def checkout(request):
    return HttpResponse("Checkout Page")