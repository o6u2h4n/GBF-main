from django.shortcuts import render
from django.http import HttpRequest
from .models import Product, Category, Toptext

# Create your views here.
def product_list(request:HttpRequest):
    """
        bu view tüm ürünleri getirir
    """
    products = Product.objects.filter(availability=True)
    categories = Category.objects.all()
    toptext = Toptext.objects.all()
    return render(request,'productlist.html',{'products':products, 'categories':categories, 'toptext':toptext })

