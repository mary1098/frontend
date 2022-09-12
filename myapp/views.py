from telnetlib import AUTHENTICATION
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def account(request):
    return render(request, 'account.html')

def frontpage(request):
    return render(request, 'frontpage.html')

def cart(request):
    return render(request, 'cart.html')

def products(request):
    return render(request, 'products.html')

def productdetails(request):
    return render(request, 'productdetails.html')

def productdetails2(request):
    return render(request, 'productdetails2.html')

def productdetails3(request):
    return render(request, 'productdetails3.html')

def productdetails4(request):
    return render(request, 'productdetails4.html')

def productdetails5(request):
    return render(request, 'productdetails5.html')

def productdetails6(request):
    return render(request, 'productdetails6.html')

def productdetails7(request):
    return render(request, 'productdetails7.html')

def productdetails8(request):
    return render(request, 'productdetails8.html')