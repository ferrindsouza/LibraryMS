from django.contrib.auth.models import User 
from django.db import models

# Create your models here. 
from book.models import Book
from useraccounts.models import Profile


class BookOrder(models.Model):
    book_id = models.IntegerField(primary_key=True, default=1)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    date_out = models.DateTimeField(editable=True)
    due_date = models.DateTimeField(editable=True) 
    delete = models.BooleanField(default=False)

