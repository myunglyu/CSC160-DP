from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import customer, STUserAccount

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
        model = STUserAccount
        fields = ["username", "first_name", "last_name", "email"]

class ProfileForm(forms.ModelForm):
    state = forms.ChoiceField (choices=[('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),('AR', 'Arkansas'),('CA', 'California'),('CO', 'Colorado'),('CT', 'Connecticut'),('DE', 'Delaware'),('FL', 'Florida'),('GA', 'Georgia'),('HI', 'Hawaii'),('ID', 'Idaho'),('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),('MI', 'Michigan'),('MN', 'Minnesota'),('MS', 'Mississippi'),('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),('NV', 'Nevada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),('ND', 'North Dakota'),('OH', 'Ohio'),('OK', 'Oklahoma'),('OR', 'Oregon'),('PA', 'Pennsylvania'),('RI', 'Rhode Island'),('SC', 'South Carolina'),('SD', 'South Dakota'),('TN', 'Tennessee'),('TX', 'Texas'),('UT', 'Utah'),('VT', 'Vermont'),('VA', 'Virginia'),('WA', 'Washington'),('WV', 'West Virginia'),('WI', 'Wisconsin'),('WY', 'Wyoming')])
    class Meta:
        model = STUserAccount
        fields = ["profile_pic", "first_name", "last_name", "email", "phone", "street", "city", "state", "zip"]

# class UserEditForm1(forms.ModelForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ["first_name", "last_name", "email"]

# class UserEditForm2(forms.ModelForm):
#     class Meta:
#         model = userprofile2
#         fields = ["profile_pic", "phone"]

# class AddressForm(forms.ModelForm):
#     state = forms.ChoiceField (choices=[
#             ('AL', 'Alabama'),
#             ('AK', 'Alaska'),
#             ('AZ', 'Arizona'),
#             ('AR', 'Arkansas'),
#             ('CA', 'California'),
#             ('CO', 'Colorado'),
#             ('CT', 'Connecticut'),
#             ('DE', 'Delaware'),
#             ('FL', 'Florida'),
#             ('GA', 'Georgia'),
#             ('HI', 'Hawaii'),
#             ('ID', 'Idaho'),
#             ('IL', 'Illinois'),
#             ('IN', 'Indiana'),
#             ('IA', 'Iowa'),
#             ('KS', 'Kansas'),
#             ('KY', 'Kentucky'),
#             ('LA', 'Louisiana'),
#             ('ME', 'Maine'),
#             ('MD', 'Maryland'),
#             ('MA', 'Massachusetts'),
#             ('MI', 'Michigan'),
#             ('MN', 'Minnesota'),
#             ('MS', 'Mississippi'),
#             ('MO', 'Missouri'),
#             ('MT', 'Montana'),
#             ('NE', 'Nebraska'),
#             ('NV', 'Nevada'),
#             ('NH', 'New Hampshire'),
#             ('NJ', 'New Jersey'),
#             ('NM', 'New Mexico'),
#             ('NY', 'New York'),
#             ('NC', 'North Carolina'),
#             ('ND', 'North Dakota'),
#             ('OH', 'Ohio'),
#             ('OK', 'Oklahoma'),
#             ('OR', 'Oregon'),
#             ('PA', 'Pennsylvania'),
#             ('RI', 'Rhode Island'),
#             ('SC', 'South Carolina'),
#             ('SD', 'South Dakota'),
#             ('TN', 'Tennessee'),
#             ('TX', 'Texas'),
#             ('UT', 'Utah'),
#             ('VT', 'Vermont'),
#             ('VA', 'Virginia'),
#             ('WA', 'Washington'),
#             ('WV', 'West Virginia'),
#             ('WI', 'Wisconsin'),
#             ('WY', 'Wyoming')
#         ])
#     class Meta:
#         model = address
#         fields = ["street", "city", "state", "zip"]
