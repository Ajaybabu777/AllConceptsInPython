from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@csrf_exempt
def register(request):
    try:
        if request.method != "POST":
            raise Exception("method not allowed", status.HTTP_405_METHOD_NOT_ALLOWED)
        
        else:
            data = json.loads(request.body)

            esmail = data["email"]
            usalname = data["username"]
            passworddddd = data["password"]

            if not esmail or not usalname or not passworddddd:
                raise Exception("Data not passed or incorrect data passed", status.HTTP_400_BAD_REQUEST)
            
            else:
                user = User.objects.create_user(username = usalname, password = passworddddd, email = esmail)
                user.save()

                return JsonResponse({
                    "status":"Success",
                    "message":f"User {usalname} registered"
                    
                }, status = status.HTTP_201_CREATED)
    
    except Exception as ex:
        return JsonResponse({
            "status":"failed",
            "message":str(ex)
        })
    
@csrf_exempt
def login(request):
    try:
        if request.method != "POST":
            raise Exception("method not allowed", status.HTTP_405_METHOD_NOT_ALLOWED)
        
        else:
            data = json.loads(request.body)
            usalname = data["username"]
            passworddddd = data["password"]

            if not usalname or not passworddddd:
                raise Exception("Data not passed or incorrect data passed", status.HTTP_400_BAD_REQUEST)
            
            else:
                user = authenticate(request, username= usalname, password = passworddddd)

                if user is not None:
                    refrest = RefreshToken.for_user(user)

                    return JsonResponse({
                        "refreshToken":str(refrest),
                        "accesstoken":str(refrest.access_token)
                    })


            
    except Exception as ex:
        return JsonResponse({
            "status":"failed",
            "message":str(ex)
        })


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

@csrf_exempt
def updateAuthor(request):
    if request.method != 'PATCH':
        return JsonResponse({
            "message":"Method not allowed"
        },status = status.HTTP_405_METHOD_NOT_ALLOWED)
    

    else:
        body = json.loads(request.body)
        authorid = body['authorId']
        newName = body['newName']

        auther = Author.objects.filter(id = authorid)

        if not auther:
            return JsonResponse({
                "message":"Author not found"
            }, status = status.HTTP_404_NOT_FOUND)
        
        else:
            autheer = Author.objects.get(id = authorid)
            oldName = autheer.name
            autheer.name = newName
            autheer.save()
            

            return JsonResponse({
                "message":"Author name updated"
            }, status = status.HTTP_200_OK)
        
@csrf_exempt
def deleteAuthor(request):
    if request.method != 'DELETE':
        return JsonResponse({
            "message":"Method not allowed"
        },status = status.HTTP_405_METHOD_NOT_ALLOWED)
    
    body = json.loads(request.body)
    authorid = body['authorId']
    auther = Author.objects.filter(id = authorid)

    if not auther:
        return JsonResponse({
            "message":"Author not found"
        }, status = status.HTTP_404_NOT_FOUND)
    
    else:
        autheer = Author.objects.get(id = authorid)
        autheer.delete()
        

        return JsonResponse({
            "message":"Author deleted"
        }, status = status.HTTP_200_OK)
