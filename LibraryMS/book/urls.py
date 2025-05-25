from django.urls import path, include 
from . import views
app_name = 'book' 
urlpatterns = [
path('update/<book_id>', views.update_book), 
path('delete/<int:book_id>', views.delete_book), 
path('search_books', views.search_books, name="search_books"), 
path('upload_book', views.upload_book, name='upload_book'), 
path('book_info/<book_id>/', views.book_info, name='book_info'), 
path('homepage', views.homepage, name='homepage'),

]
