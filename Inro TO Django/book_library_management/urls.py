from django.urls import path
from .views import create_author, create_book

urlpatterns = [
    path('author/create', create_author),
    path('book/create', create_book),
]
