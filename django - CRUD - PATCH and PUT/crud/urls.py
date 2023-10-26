from django.urls import path, include
from .views import *

urlpatterns = [
    path("postTask", postTask),
    path("putTask", putTask),
    path("patchTask",patchTask)
]