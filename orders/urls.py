from django.urls import path
from .views import checkout, orderprocess, ordersuccess

urlpatterns = [
    path('cart/checkout/', checkout, name="checkout"),
    path('cart/orderprocess', orderprocess, name="orderprocess"),
    path('cart/ordersuccess', ordersuccess, name="ordersuccess"),
    # path('cart/orderprocess2', orderprocess2, name="orderprocess2"),
    # path('cart/ordersubmit', ordersubmit, name="ordersubmit"),
    # path('save-cart/', save_cart, name='save_cart'),
]
