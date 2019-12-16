from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    imageLink = models.CharField(max_length=900)


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400)
    item = models.TextField(max_length=400)
    fullfilled = models.BooleanField()


