from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
# Create your views here.


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)
