from django.urls import path
from .views import *

urlpatterns = [
    path('author/create', create_author),
    path('book/create', create_book),
    path('books/author/<int:author_id>/',getBookNames),
    path('deleteAuthor/',deleteAuthor),
    path('register', register),
    path('login', login)
]
