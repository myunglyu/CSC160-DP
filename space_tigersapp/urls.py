from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('customers/', views.customers),
    path('customers/new', views.newcustomer.as_view()),
    path('customers/<pk>/update', views.updatecustomer.as_view()),
    path('customers/<pk>/delete', views.deletecustomer.as_view()),
    # path('success/', views.success_view, name='success'),
]