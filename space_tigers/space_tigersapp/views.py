from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products': Product_list}) 

def new(request):
    return HttpResponse('New Page')
