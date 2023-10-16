from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Author, Book

@csrf_exempt
def create_author(request):
    bodyToJson = json.loads(request.body)
    authorNameFromFrontEnd = bodyToJson['name']

    author = Author(name = authorNameFromFrontEnd) # ORM
    author.save()
    
    return JsonResponse({
        "message": f'{authorNameFromFrontEnd} added to Author table'
    })

@csrf_exempt
def create_book(request):
    bodyToJson = json.loads(request.body)
    
    idOfAuhor = bodyToJson['author_id']
    author = Author.objects.get(id = idOfAuhor)
    if not author:
        return JsonResponse({
            "message":"Author ID not present in DB please check again"
        })

    namesOfBooks = bodyToJson['books_Names']

    bookList = []

    for bookName in namesOfBooks:
        bookList.append(bookName)
        book = Book.objects.create(title =bookName, author =author  )

    return JsonResponse({
        "message":f"{namesOfBooks} have been saved for the {author.name} in Book Table"
    })


