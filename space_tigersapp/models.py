from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField(max_length=2083)

class customer(models.Model):
    fname = models.CharField(max_length=255)
    mi = models.CharField(max_length=1)
    lname = models.CharField(max_length=255)
    email = models.EmailField(("Email"), max_length=254)
    phone = models.CharField(("Phone Number"), max_length=10)
    image_url = models.URLField(max_length=2083)
