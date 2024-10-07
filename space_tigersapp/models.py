from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField("Product Name", max_length=255)
    price = models.FloatField()
    stock = models.IntegerField("Stock Qty")
    image_url = models.CharField("Image URL", max_length=2083)

class customer(models.Model):
    fname = models.CharField("First Name", max_length=255)
    mi = models.CharField("Middle Initial", max_length=1, blank=True, default="")
    lname = models.CharField("Last Name", max_length=255)
    email = models.EmailField("E-mail", max_length=255)
    phone = models.CharField("Phone Number", max_length=10)
    image_url = models.CharField("Image URL", max_length=2083)