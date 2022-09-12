from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.frontpage, name='myapp'),
    path('frontpage', views.frontpage, name='frontpage'),
    path('account', views.account, name='account'),
    path('cart', views.cart, name='cart'),
    path('products', views.products, name='products'),
    path('productdetails', views.productdetails, name='productdetails'),
    path('productdetails2', views.productdetails2, name='productdetails2'),
    path('productdetails3', views.productdetails3, name='productdetails3'),
    path('productdetails4', views.productdetails4, name='productdetails4'),
    path('productdetails5', views.productdetails5, name='productdetails5'),
    path('productdetails6', views.productdetails6, name='productdetails6'),
    path('productdetails7', views.productdetails7, name='productdetails7'),
    path('productdetails8', views.productdetails8, name='productdetails8'),
]