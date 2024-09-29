from django.shortcuts import render
from django.http import HttpResponse
from .models import product, customer
from .forms import customerform



# Create your views here.

product_list = product.objects.all()
customer_list = customer.objects.all()

def index(request):
    return render(request, 'index.html', {'products': product_list})

def customers(request):
    return render(request, 'customers.html', {'customers': customer_list})

from django.shortcuts import render, redirect

def newcustomer(request):
    if request.method == 'POST':
        form = customerform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("window.alert(success);", mime_type="application/x-javascript")
    else:
        form = customerform()
    return render(request, 'newcustomer.html', {'form': form})
