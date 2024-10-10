from django.contrib import admin
from .models import Product, customer

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product)

class customerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'mi', 'lname', 'email', 'phone')

admin.site.register(customer)