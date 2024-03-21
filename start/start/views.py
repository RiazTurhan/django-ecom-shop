from django.http import HttpResponse
from django.shortcuts import render 

def homePage(request):
  return render (request, 'index.html')

def about(request):
  return render (request , 'about.html')


def cart(request):
  return render (request, 'cart.html')

def checkout(request):
  return render (request , 'checkout.html')

def contact(request):
  return render (request , 'contact-us.html')

def gallery(request):
  return render (request , 'gallery.html')


def account(request):
  return render (request, 'my-account.html')

def shopDetails(request):
  return render (request , 'shop-detail.html')


def shop(request):
  return render (request , 'shop.html')

def wishlist(request):
  return render (request , 'wishlist.html')