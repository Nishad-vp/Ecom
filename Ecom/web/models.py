from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image=models.ImageField(upload_to='media/product_image')

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    address =models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phone =models.IntegerField()
    email =models.EmailField(max_length=50)
    date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    image =models.ImageField(upload_to='media/order_image')
    qunatity=models.IntegerField() 
    price=models.FloatField() 
    total=models.IntegerField()
    paid=models.BooleanField(default=False)
    


