from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderHistory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def create_sample_order(request):
    sample_order = OrderHistory(
        Customer=User.objects.get(username='sample_user'),
        ItemName='Sample Item',
        Price=9.99,
        Qty=1,
        image_url='http://example.com/sample.jpg'
    )
    sample_order.save()
    # return HttpResponse('Sample order created!')
    return render(request, 'democheckout.html')

