from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('customers', views.customers),
    path('newcustomer/', views.newcustomer)
    # path('success/', views.success_view, name='success'),
]