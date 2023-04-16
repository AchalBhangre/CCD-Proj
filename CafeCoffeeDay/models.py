from django.db import models

# Create your models here.

class CafeCoffeeDay(models.Model):
    
    coffeeName = models.CharField(max_length=200)
    fName = models.CharField(max_length=300)
    address = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.fName
        
class MenuItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_ingredients = models.TextField()
    item_category = models.CharField(max_length=50, choices=(
        ('appetizers', 'Appetizers'),
        ('entrees', 'Entrees'),
        ('desserts', 'Desserts'),
        ('drinks', 'Drinks'),
    ))
    def __str__(self):
        return self.item_name

