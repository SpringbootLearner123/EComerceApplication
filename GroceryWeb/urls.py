"""GroceryWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from General import views
from AdminZone import views as asection



urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('brands/',views.brandf),
    path('househ/',views.household),
    path('vegi/',views.vegetables),
    path('kitchen/',views.kitchen),
    path('sftdrink/',views.softdrink),
    path('pets/',views.petfood),
    path('frozen/',views.frozen),
    path('breads/',views.breadb),
    path('loginreg/',views.loginreg),
    path('loginData/',views.loginData),
    path('dashboard/',asection.dashboard),
    path('contactmgt/',asection.contactmgmt),
    path('ordermgmt/',asection.ordermgmt),
    path('addprod/',asection.addproduct),
    path('productmgmt/',asection.productmgmt),
    path('Alogout/',asection.Alogout),
    path('signupdata/',views.signupdata),

]
