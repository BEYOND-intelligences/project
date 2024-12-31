from django.db import models

# Create your models here.

class Car (models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)

class Product (models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    photo = models.ImageField(upload_to ='photos/%y/%m/%d') 
    active = models.BooleanField(default=True)