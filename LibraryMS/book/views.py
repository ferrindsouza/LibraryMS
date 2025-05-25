import tkinter
from tkinter.tix import Tk 
import tkinter.messagebox

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import BookCreate, BookUpdate, BookUpdateExtra 
from .models import Book
from bookorders.models import BookOrder


def search_books(request): 
    books = Book.objects.all()
    return render(request, 'search_books.html', {'books': books})


def update_book(request, book_id):
    context = {'updatebk': BookUpdate(), 'updatebkextra': BookUpdateExtra()} 
    if request.method == 'POST':
        book_sel = Book.objects.get(pk=book_id) 
        book_sel_extra = BookOrder.objects.get(pk=book_id)
        updatebk = BookUpdate(request.POST, request.FILES, instance=book_sel) 
        updatebkextra = BookUpdateExtra(request.POST, request.FILES,instance=book_sel_extra)
 
        if updatebk.is_valid(): 
            updatebk.save(['quantity', 'isissued', 'owner'])
            updatebkextra.save(['date_out', 'due_date', 'owner']) 
            root = Tk()
            tkinter.messagebox.showinfo('Popup Window(Title)', 'Book Issued Successfully')
            root.mainloop()
            return redirect('/book/search_books') 
        else:
            return HttpResponse("your form is wrong, reload on <a href = '/book/search_books'>reload</a>")
    else:
        return render(request, 'update_form.html', {'update_form': context.items()})


def upload_book(request): 
    uploadbk = BookCreate()
    if request.method == 'POST':
        uploadbk = BookCreate(request.POST, request.FILES) 
        if uploadbk.is_valid():
            uploadbk.save()
            return redirect('/book/search_books') 
        else:
            return HttpResponse("your form is wrong, reload on <a href = 'search_books'>reload</a>")
    else:
        return render(request, 'upload_form.html', {'upload_form': uploadbk})


def book_info(request, book_id):
    selected_book = Book.objects.get(pk=book_id)
    return render(request, 'book_info.html', {'book_info': selected_book})


def homepage(request): 
    return redirect('/')


def delete_book(request, book_id): 
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(pk = book_id)
    # book_sel_extra = BookOrder.objects.get(pk =book_id) 
    except Book.DoesNotExist:
        return redirect('/book/search_books') 
    book_sel.delete()
    # book_sel_extra.delete() 
    root = Tk()
    tkinter.messagebox.showinfo('Popup Window(Title)', 'Book Deleted Successfully')
    
    root.mainloop()
    return redirect('/book/search_books')

