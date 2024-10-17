import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from space_tigersapp.models import Product, STUserAccount
from django. http import JsonResponse
from django.contrib import messages
from django.urls import reverse, reverse_lazy
import urllib.parse
from .forms import CustomerOrderForm
import json
from datetime import datetime
from django.views.decorators.cache import never_cache
from cart.cart import Cart

@login_required
def checkout(request):

    encoded_data = request.POST.get('cart_data', '')
    decoded_data = urllib.parse.unquote(encoded_data)
    # print(decoded_data)
   
    itemlist = decoded_data.split("]")
    itemlist.pop()
    itemset = [item.split('@') for item in itemlist]
    
    # print(userpk)
    # print(cartlenth)
    # print(itemsdata)
    # print(itemlist)
    # print(itemset)

    ordersummary = []
    OrderTotal = 0
    
    for item in itemset:
        
        ProductID, Quantity = map(int, item)
        product = Product.objects.get(id=ProductID)
        OrderTotal += (product.price * Quantity)
        ordersummary.append({'product':product, 'quantity':Quantity, 'total':product.price * Quantity})

    context = {
        'encoded_data': encoded_data,
        'ordersummary': ordersummary,
        'ordertotal': OrderTotal,
    }

    # print(context)

    return render(request, 'ordersummary.html', context)

@login_required
def orderprocess(request):
    encoded_data = request.POST.get('encoded_data', '')
    decoded_data = urllib.parse.unquote(encoded_data)
    address = request.POST.get('address')

    itemlist = decoded_data.split("]")
    itemlist.pop()
    itemset = [item.split('@') for item in itemlist]

    print(itemset)

    if request.method == 'POST':
        order = CustomerOrderForm(request.POST)
        if order.is_valid():
            neworder = order.save()
            ordernumber = neworder.OrderNumber
            context = {"ordernumber":ordernumber}
            url = reverse_lazy('ordersuccess') + f'?ordernumber={ordernumber}'
            return redirect(url)
        else:
            order = CustomerOrderForm()

    context = {
        'address': address,
        'order': order,
        'itemset': itemset,
        'encoded_data': encoded_data
    }

    return render(request, 'orderprocess.html', { "context": context })

@login_required
def ordersuccess(request):
    ordernumber = request.GET.get('ordernumber')
    Cart(request).clear()
    context = {
        'ordernumber': ordernumber,
    }
    return render(request, 'ordersuccess.html', context)