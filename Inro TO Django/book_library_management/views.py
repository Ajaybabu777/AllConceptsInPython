from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Author, Book
from rest_framework import status

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


@csrf_exempt
def getBookNames(request, author_id):
    if request.method != "GET":
        return JsonResponse({
            "message":"method not supported"
        }, status = status.HTTP_405_METHOD_NOT_ALLOWED)
    else:

        authorIdObj = Author.objects.filter(id = author_id)

        if not authorIdObj:
            return JsonResponse({
                "message":"Author not found"
            }, status = status.HTTP_404_NOT_FOUND)
        
        books = Book.objects.filter(author_id = author_id)
        bookList = []

        for book in books:
            bookList.append(book.title)

        authorId = None

        for book in books:
            authorId = book.author_id
            break
        
        authorName  = Author.objects.get(id = author_id).name


        return JsonResponse({
            "message":"Book queryed successfully",
            "authorName":authorName,
            "data":bookList
        })

