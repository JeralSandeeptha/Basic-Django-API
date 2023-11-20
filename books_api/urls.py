from django.contrib import admin
from django.urls import path
from books_api.views import getAllBooks, deleteBook, updateBook, getSingleBook, createBook;

urlpatterns = [
    path('getbooks/', getAllBooks, name="Get All Books"),
    path('createbook/', createBook, name="Create New Book"),
    path('getbook/<int:pk>/', getSingleBook, name="Get Single Book"),
    path('updatebook/<int:pk>/', updateBook, name="Update Book"),
    path('deletebook/<int:pk>/', deleteBook, name="Delete Book"),
]