from django.db import models
from space_tigersapp.models import STUserAccount

# Create your models here.

class OrderHistory(models.Model):
    OrderNumber = models.AutoField("Order Number", primary_key=True)
    Customer = models.ForeignKey(STUserAccount, on_delete=models.CASCADE, null=True)
    ItemName = models.TextField("Item Name", null=True)
    Price = models.FloatField("Price", null=True)
    Qty = models.IntegerField("Stock Qty", null=True)
    image_url = models.CharField("Image URL", max_length=2083, null=True)