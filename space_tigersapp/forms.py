from django import forms
from .models import customer

class customerform(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['fname', 'mi', 'lname', 'email', 'phone', 'image_url']
        labels = {
            "fname": ("First Name"),
            "mi": ("Middle Initial"),
            "lname": ("Last Name"),
            "email": ("E-mail"),
            "phone": ("Phone Number"),
            "image_url": ("Image URL")
        }
    
