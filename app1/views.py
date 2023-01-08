from django.shortcuts import render
from django.http import HttpResponse
 

def first(request):
    return HttpResponse('this is app1 data')