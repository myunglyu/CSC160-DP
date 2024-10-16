import os
from django.shortcuts import render, redirect
from space_tigersapp.models import Product
from django. http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

def checkout(request):

    encoded_data = request.POST.get('data', '')
    decoded_data = urllib.parse.unquote(encoded_data)
    # print(decoded_data)

    userpk = decoded_data.split("%")[0]
    # cartlenth = decoded_data.split("%")[1]
    itemsdata = decoded_data.split("%")[2]
    
    itemlist = itemsdata.split("]")
    itemlist.pop()
    itemset = [item.split('@') for item in itemlist]
    
    # print(userpk)
    # print(cartlenth)
    # print(itemsdata)
    # print(itemlist)
    print(itemset)

    ordersummary = []
    for item in itemset:
        ProductID, Quantity = map(int, item)
        product = Product.objects.get(id=ProductID)
        ordersummary.append({'product':product, 'quantity':Quantity, 'total':product.price * Quantity})

    context = {
        'userid': userpk,
        'ordersummary': ordersummary
    }

    return render(request, 'ordersummary.html', context)

