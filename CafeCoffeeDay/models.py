from django.db import models

# Create your models here.

class CafeCoffeeDay(models.Model):
    
    coffeeName = models.CharField(max_length=200)
    fName = models.CharField(max_length=300)
    address = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.fName