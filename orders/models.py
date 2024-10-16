from django.db import models
from space_tigersapp.models import STUserAccount, Product

# Create your models here.

class CustomerOrders(models.Model):
    OrderNumber = models.AutoField("Order Number", primary_key=True)
    Customer = models.ForeignKey(STUserAccount, on_delete=models.CASCADE, null=True)
    OrderDate = models.TimeField("Date Ordered")
    # image_url = models.CharField("Image URL", max_length=2083, null=True)
    # ItemName = models.TextField("Item Name", null=True)
    # Price = models.FloatField("Price", null=True)
    # Qty = models.IntegerField("Stock Qty", null=True)

class OrderDetail(models.Model):
    OrderNumber = models.ForeignKey(CustomerOrders, on_delete=models.CASCADE, null=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Qty = models.IntegerField("Stock Qty", null=True)
    ShippingAddress = models.TextField("Shipping Address")