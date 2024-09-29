from django import forms
from .models import customer

class customerform(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['fname', 'mi', 'lname', 'email', 'phone', 'image_url']
