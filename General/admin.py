from django.contrib import admin
from General.models import contactModel,userdata,ALogin,ProductModel,signupdata
# Register your models here.

mlist = [contactModel,userdata,ALogin,ProductModel,signupdata]
for x in mlist:
    admin.site.register(x)