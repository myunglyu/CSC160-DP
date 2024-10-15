from django.contrib import admin
from .models import Product, customer, STUserAccount
from orders.models import OrderHistory

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product)

class customerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'mi', 'lname', 'email', 'phone')

admin.site.register(customer)

admin.site.register(OrderHistory)

admin.site.register(STUserAccount)