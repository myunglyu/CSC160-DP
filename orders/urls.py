from django.urls import path
from .views import checkout

urlpatterns = [
    path('cart/checkout/', checkout, name="checkout"),
    # path('save-cart/', save_cart, name='save_cart'),
]
