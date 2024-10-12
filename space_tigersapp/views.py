from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .models import Product, customer
from .forms import SignUpForm, UserEditForm
from django.urls import reverse_lazy
from orders.models import OrderHistory
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.views.generic import View


def index(request):
    product_list = Product.objects.all()
    return render(request, 'index.html', {'products': product_list})

@login_required
@permission_required('space_tigersapp.view_customers', login_url='/login/')
def customers(request):
    customer_list = customer.objects.all()
    return render(request, 'customers.html', {'customers': customer_list})

class newcustomer(PermissionRequiredMixin, CreateView):
    permission_required = 'space_tigersapp.add_customers'
    login_url = '/accounts/login/'
    template_name = "customer_new.html"
    model = customer
    fields = ["fname", "mi", "lname", "email", "phone", "image_url"]
    template_name_suffix = "_new"
    success_url = "/customers"

class updatecustomer(PermissionRequiredMixin, UpdateView):
    permission_required = 'space_tigersapp.change_customers'
    login_url = '/accounts/login/'
    template_name = "customer_update_form.html"
    model = customer
    fields = ["fname", "mi", "lname", "email", "phone", "image_url"]
    template_name_suffix = "_update_form"
    success_url = "/customers"

class deletecustomer(PermissionRequiredMixin, DeleteView):
    permission_required = 'space_tigersapp.delete_customers'
    login_url = '/accounts/login/'
    template_name = "customer_delete.html"
    model = customer
    template_name_suffix = "delete"
    success_url = "/customers"

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def ProfileView(request):
    orders = OrderHistory.objects.filter(Customer=request.user)
    return render(request, "accounts/profile.html", {'orders': orders})

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = UserEditForm
    success_url = reverse_lazy("profile")
    template_name = "accounts/edit.html"

    def get_object(self, queryset=None):
        return self.request.user

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model=User
    success_url = "/"
    template_name = "accounts/delete.html"

    def get_object(self, queryset=None):
        return self.request.user

class ChangePassword(PasswordChangeView):
    success_url = reverse_lazy("profile")
    template_name = "registration/password_change_form.html"
