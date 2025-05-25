from django import forms 
from .models import Book
from bookorders.models import BookOrder

class BookCreate(forms.ModelForm): 
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'author_name', 'edition_year', 'quantity', 'book_img']

class BookUpdate(forms.ModelForm): 
    class Meta:
        model = Book
        # model = BookOrder
        fields = ['quantity', 'isissued', 'owner']
 
class BookUpdateExtra(forms.ModelForm): 
    class Meta:
        model = BookOrder
        fields = ['date_out', 'due_date', 'owner']

