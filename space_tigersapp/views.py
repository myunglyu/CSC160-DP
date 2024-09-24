from django.shortcuts import render
from django.http import HttpResponse
from .models import product, customer

# Create your views here.

product_list = product.objects.all()
customer_list = customer.objects.all()

def index(request):
    return render(request, 'index.html', {'products': product_list})

def new(request):
    return HttpResponse('New Page')

def customers(request):
    return render(request, 'customers.html', {'customers': customer_list})