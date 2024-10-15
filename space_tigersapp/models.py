import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.deconstruct import deconstructible
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

@deconstructible
class PathAndRename:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f'profile.{ext}'
        return os.path.join(self.path, str(instance.id), filename)

class STUserAccount(AbstractUser):
    profile_pic = models.ImageField("Profile Picture", upload_to=PathAndRename('profile_pictures/'), blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=15, blank=True, null=True)
    street = models.CharField("Street", max_length=255, blank=True, null=True)
    city = models.CharField("City", max_length=255, blank=True, null=True)
    state = models.CharField("State", max_length=20, blank=True, null=True)
    zip = models.CharField("Zip", max_length=5, blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            this = STUserAccount.objects.get(id=self.id)
            if this.profile_pic != self.profile_pic:
                this.profile_pic.delete(save=False)
        except:
            pass
        super(STUserAccount, self).save(*args, **kwargs)
    
# class userprofile2(models.Model):
#     userID = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField (blank=True)
#     phone = models.CharField("Phone Number", max_length=15, blank=True)

# class address(models.Model):
#     userID = models.ForeignKey(User, on_delete=models.CASCADE)
#     street = models.CharField ("Street", max_length=255, blank=True)
#     city = models.CharField ("City", max_length=255, blank=True)
#     state = models.CharField ("State", max_length=20, blank=True)
#     zip = models.DecimalField ("Zip", max_digits=5, decimal_places=0, blank=True)