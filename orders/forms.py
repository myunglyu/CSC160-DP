from django import forms
from .models import CustomerOrders

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrders
        fields = ['Customer', 'ShippingAddress', 'ItemsOrdered']
