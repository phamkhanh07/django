from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def greeting(request):
    return HttpResponse("Hello World !!")