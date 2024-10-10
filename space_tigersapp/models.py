from django.db import models
import datetime


# Create your models here.

class Product(models.Model):
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

class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	customer = models.ForeignKey(customer, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	address = models.CharField(max_length=100, default='', blank=True)
	phone = models.CharField(max_length=20, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.product