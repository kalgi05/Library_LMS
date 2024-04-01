"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard, name='Home'),
    path('books', views.Books, name='Books'),
    path('contact', views.Contact, name='Contact'),
    path('login', views.Login, name='Login'),
    path('logout', views.Logout, name='Logout'),
    path('register', views.Register, name='Register'),
    path('contact' , views.Contact , name='Contact'),
    path('product-details' , views.product_details, name='product-details'),
    path('communication', views.communication, name='communication'),
    path('poetry', views.poetry, name='poetry'),
    path('inspiration', views.inspiration, name='inspiration'),
    path('details1', views.details1, name='details1'),
    path('details2', views.details2, name='details2'),
    path('details3', views.details3, name='details3'),
    path('details4', views.details4, name='details4'),
    path('details5', views.details5, name='details5'),
    path('details6', views.details6, name='details6'),
    path('details7', views.details7, name='details7'),
    # path('registere', views.Generate, name='QRRegister')
]
