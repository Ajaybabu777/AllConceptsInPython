from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task
from django.views.decorators.http import require_http_methods

# Create your views here.

@csrf_exempt
@require_http_methods(["POST"])
def postTask(request):
    try:
        data = json.loads(request.body)
        titli = data['title']
        descra = data['description']

        task = Task(title = titli, description = descra)
        task.save()

        return JsonResponse({
            "message":"data save successfully"
        })

    except Exception as ex:
        return JsonResponse({
            "message":str(ex)
        })

@csrf_exempt
@require_http_methods(["PUT"])
def putTask(request):
    try:
        data = json.loads(request.body)
        titli = data['title']
        descra = data['descra']
        idFromInsomnia = data['id']

        task = Task.objects.get(id = idFromInsomnia)

        if task:
            task.title = titli
            task.description = descra

            task.save()

            return JsonResponse({
                "message":"PUT successfull"
            })


    except Exception as ex:
        return JsonResponse({
            "message":str(ex)
        })
    

@csrf_exempt
@require_http_methods(["PATCH"])
def patchTask(request):
    try:
        data = json.loads(request.body)
        idFromInsomnia = data['id']

        task = Task.objects.get(id = idFromInsomnia)

        if task:
            if 'title' in data and data['title'] != "":
                task.title = data['title']
            if 'descra' in data and data['descra'] != "":
                task.description = data['descra']

            task.save()

            return JsonResponse({
                "message":"patch successfull"
            })


    except Exception as ex:
        return JsonResponse({
            "message":str(ex)
        })