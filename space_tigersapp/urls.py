from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('customers/', views.customers),
    path('newcustomer/', views.newcustomer),
    path('customers/<pk>/update', views.updatecustomer.as_view()),
    path('customers/<pk>/delete', views.deletecustomer.as_view()),
    # path('success/', views.success_view, name='success'),
]