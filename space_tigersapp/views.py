from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import product, customer
from .forms import SignUpForm
from django.urls import reverse_lazy


def index(request):
    product_list = product.objects.all()
    return render(request, 'index.html', {'products': product_list})

# @login_required
# @permission_required
def customers(request):
    customer_list = customer.objects.all()
    return render(request, 'customers.html', {'customers': customer_list})

class newcustomer(CreateView):
    template_name = "customer_new.html"
    model = customer
    fields = ["fname", "mi", "lname", "email", "phone", "image_url"]
    template_name_suffix = "_new"
    success_url = "/customers"

class updatecustomer(UpdateView):
    template_name = "customer_update_form.html"
    model = customer
    fields = ["fname", "mi", "lname", "email", "phone", "image_url"]
    template_name_suffix = "_update_form"
    success_url = "/customers"

class deletecustomer(DeleteView):
    template_name = "customer_delete.html"
    model = customer
    template_name_suffix = "delete"
    success_url = "/customers"

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

