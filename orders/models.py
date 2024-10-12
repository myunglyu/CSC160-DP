from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OrderHistory(models.Model):
    OrderNumber = models.AutoField("Order Number", primary_key=True)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ItemName = models.TextField("Item Name")
    Price = models.FloatField("Price")
    Qty = models.IntegerField("Stock Qty")
    image_url = models.CharField("Image URL", max_length=2083) 