from django.contrib import admin
from django.urls import path
from books_api.views import getAllBooks, deleteBook, updateBook, getSingleBook, createBook;

urlpatterns = [
    path('getbooks/', getAllBooks),
    path('createbook/', createBook),
    path('getbook/<int:pk>/', getSingleBook),
    path('updatebook/<int:pk>/', updateBook),
    path('deletebook/<int:pk>/', deleteBook),
]