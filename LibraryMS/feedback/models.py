from django.db import models 

# Create your models here.
from django.forms import forms


class Product(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self): 
        return self.name

class Feedback(models.Model):
    Customer_name = models.CharField(max_length=100) 
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.customer_name
