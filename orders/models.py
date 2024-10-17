from django.db import models
from space_tigersapp.models import STUserAccount, Product
from datetime import datetime

# Create your models here.

class CustomerOrders(models.Model):
    OrderNumber = models.AutoField("Order Number", primary_key=True)
    Customer = models.ForeignKey(STUserAccount, on_delete=models.CASCADE, null=True)
    OrderDate = models.DateTimeField("Date Ordered", default=datetime.now)
    ShippingAddress = models.CharField("Shipping Address", max_length=255, null=True)
    ItemsOrdered = models.JSONField("ItemsOrdered", default=dict)
    # ItemName = models.TextField("Item Name", null=True)
    # Price = models.FloatField("Price", null=True)
    # Qty = models.IntegerField("Stock Qty", null=True)

# class OrderDetail(models.Model):
#     OrderNumber = models.ForeignKey(CustomerOrders, on_delete=models.CASCADE, null=True)
#     ProductID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     Qty = models.IntegerField("Stock Qty", null=True)
