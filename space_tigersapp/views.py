from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.views.generic.edit import UpdateView, DeleteView
from .models import product, customer
from .forms import customerform

product_list = product.objects.all()
customer_list = customer.objects.all()

def index(request):
    return render(request, 'index.html', {'products': product_list})

def customers(request):
    return render(request, 'customers.html', {'customers': customer_list})

# @login_required
# @permission_required
def newcustomer(request):
    if request.method == 'POST':
        form = customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customers')
    else:
        form = customerform()
    return render(request, 'newcustomer.html', {'form': form})

class updatecustomer(UpdateView):
    template_name = "customer_update_form.html"
    model = customer
    fields = ["fname", "mi", "lname", "email", "phone", "image_url"]
    template_name_suffix = "_update_form"
    success_url = "/customers"

class deletecustomer(DeleteView):
    template_name = "customer_delete.html"
    model = customer
    fields = ["fname", "mi", "lname", "email", "phone", "image_url"]
    template_name_suffix = "delete"
    success_url = "/customers"