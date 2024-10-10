from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]