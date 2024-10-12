from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('', views.index),
    path('customers/', views.customers),
    path('customers/new', views.newcustomer.as_view()),
    path('customers/<pk>/update', views.updatecustomer.as_view()),
    path('customers/<pk>/delete', views.deletecustomer.as_view()),
    # path('success/', views.success_view, name='success'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/profile/', views.ProfileView, name='profile'),
    path('accounts/profile/edit', views.UserEditView.as_view(), name='editprofile'),
    path('accounts/delete/', views.AccountDeleteView.as_view(), name='deleteaccount'),
    path('accounts/profile/passwordchange', views.ChangePassword.as_view(), name='changepassword'),
    path('cart/', include('cart.urls')),
    path('product/<int:pk>', views.Product, name='product'),
]