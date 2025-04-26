from django.db import models

# Create your models here.

class contactModel(models.Model):
    name=models.CharField(max_length=50)
    mob=models.CharField(max_length=40)
    email=models.CharField(max_length=120)
    subj=models.CharField(max_length=200)
    msg=models.CharField(max_length=500)


class userdata(models.Model):
    fname=models.CharField(max_length=50)
    mob=models.CharField(max_length=40)
    lmark=models.CharField(max_length=120)
    town=models.CharField(max_length=200)
    atype=models.CharField(max_length=300)


class ALogin(models.Model):
    userid=models.CharField(max_length=120)
    passwd=models.CharField(max_length=60)

class ProductModel(models.Model):
    pname=models.CharField(max_length=120)
    pprice=models.CharField(max_length=50)
    ppic=models.FileField(upload_to="static/products/")
class signupdata(models.Model):
    susername=models.CharField(max_length=120)
    semail=models.CharField(max_length=50)
    spassword=models.CharField(max_length=20)

