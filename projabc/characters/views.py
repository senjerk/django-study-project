from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Some fine information about favorite characters.')


def tags(request):
    return HttpResponse('<h1>Tags</h1>')
