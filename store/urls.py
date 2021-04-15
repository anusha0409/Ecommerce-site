"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import signup,Login,Signup,otp_verify,Index,logout,Cart,CheckOut,OrderView,Locate,my_view_that_updates_pieFact,Wholesaler_dashboard
from .views import add_products
from django.conf.urls import url
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


urlpatterns = [
    path('', Index.as_view() , name="homepage"),
    path('signup', Signup.as_view(), name='signup'),
    path('otp_verify',otp_verify,name="otp_verification"),
    path('login', Login.as_view(), name='login'),
    path('logout',logout,name='logout'),
    path('cart', Cart.as_view(),name="cart"),
    path('check-out', CheckOut.as_view(),name="checkout"),
    path('orders',auth_middleware( OrderView.as_view()),name="orders"),
    path('locate',Locate.as_view(),name="locate"),
    path('my_view_that_updates_pieFact', my_view_that_updates_pieFact),
    path('wholesaler_dashboard' ,Wholesaler_dashboard.as_view(),name="wholesaler_dashboard"),
    path('add_products', add_products.as_view(),name='add_products')

]
