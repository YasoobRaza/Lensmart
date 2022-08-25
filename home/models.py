from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.dispatch import receiver
from django.forms import ImageField, IntegerField
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.
# class Customer(models.Model):
#     phone =models.PhoneNumberField()
#     add



class Product(models.Model):
    product_id=models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=100)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="product/images")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_phone =models.CharField(max_length=50)
    order_address= models.TextField(max_length=500)
    products= models.ManyToManyField(Product)
    order_date= models.DateField( )

    def __str__(self):
        print(self.order_id)
        return str(self.order_id)



