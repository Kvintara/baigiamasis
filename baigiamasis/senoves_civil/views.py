
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create views here.


def index(request):
    return HttpResponse("Senoves civilizacijos")


def categories(request, catid):
    return HttpResponse(f"<h1>Kategorijos</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Puslapis nerastas</h1>")