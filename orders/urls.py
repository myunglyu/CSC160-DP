from django.urls import path
from .views import create_sample_order

urlpatterns = [
    path('create-sample-order/', create_sample_order, name='create-sample-order'),
]
