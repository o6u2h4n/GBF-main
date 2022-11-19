from django.shortcuts import render
from django.http import HttpRequest
from .models import Product, Category

# Create your views here.
def product_list(request:HttpRequest):
    """
        bu view tüm ürünleri getirir
    """
    products = Product.objects.filter(availability=True)
    return render(request,'productlist.html',{'products':products})

