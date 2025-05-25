from django.contrib.auth.models import User 
from django.db import models


# Create your models here.
from useraccounts.models import Profile


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True) 
    title = models.CharField(max_length=200) 
    author_name = models.CharField(max_length=100) 
    edition_year = models.IntegerField()
    quantity = models.IntegerField()
    book_img = models.ImageField(upload_to='pics')
    issue = models.CharField(max_length=20, default="click to issue book") 
    isissued = models.BooleanField(default=False)
    description = models.CharField(max_length=200, default="No info available currently")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self): 
        return self.title
