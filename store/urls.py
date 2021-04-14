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
from .views import signup,Login,Signup,otp_verify,Index,logout,Cart
from django.conf.urls import url

urlpatterns = [
    path('', Index.as_view() , name="homepage"),
    path('signup', Signup.as_view(), name='signup'),
    path('otp_verify',otp_verify,name="otp_verification"),
    path('login', Login.as_view(), name='login'),
    path('logout',logout,name='logout'),
    path('cart', Cart.as_view(),name="cart")
]