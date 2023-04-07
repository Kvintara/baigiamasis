
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create views here.


def index(request):
    return render(request, 'senoves_civil/index.html', {'title': 'Senovės civilizacijos'})


def aksumas(request):
    return render(request, 'senoves_civil/aksumas.html', {'title': 'Aksumas'})


def armenija(request):
    return render(request, 'senoves_civil/armenija.html', {'title': 'Armenija'})


def asirija(request):
    return render(request, 'senoves_civil/asirija.html', {'title': 'Asirija'})


def cinai(request):
    return render(request, 'senoves_civil/cinai.html', {'title': 'Cinai'})


def coment(request):
    return render(request, 'senoves_civil/coment.html', {'title': 'Komentarai'})


def dzou(request):
    return render(request, 'senoves_civil/dzou.html', {'title': 'Dzou'})


def egejas(request):
    return render(request, 'senoves_civil/egejas.html', {'title': 'Egejas'})


def egiptas(request):
    return render(request, 'senoves_civil/egiptas.html', {'title': 'Egiptas'})


def elamas(request):
    return render(request, 'senoves_civil/elamas.html', {'title': 'Elamas'})


def graikija(request):
    return render(request, 'senoves_civil/graikija.html', {'title': 'Graikija'})


def hanai(request):
    return render(request, 'senoves_civil/hanai.html', {'title': 'Hanai'})


def home(request):
    return render(request, 'senoves_civil/home.html', {'title': 'Senovės civilizacijos'})


def indo_slenis(request):
    return render(request, 'senoves_civil/indo_slenis.html', {'title': 'Indo Slenis'})


def jamas(request):
    return render(request, 'senoves_civil/jamas.html', {'title': 'Jamas'})


def jemenas(request):
    return render(request, 'senoves_civil/jemenas.html', {'title': 'Jemenas'})


def kanaanas(request):
    return render(request, 'senoves_civil/kanaanas.html', {'title': 'Kanaanas'})


def kusas(request):
    return render(request, 'senoves_civil/kusas.html', {'title': 'Kusas'})


def libija(request):
    return render(request, 'senoves_civil/libija.html', {'title': 'Libija'})


def maurja(request):
    return render(request, 'senoves_civil/maurja.html', {'title': 'Maurja'})


def mazoji_azija(request):
    return render(request, 'senoves_civil/mazoji_azija.html', {'title': 'Mazoji Azija'})


def mesopotamija(request):
    return render(request, 'senoves_civil/mesopotamija.html', {'title': 'Mesopotamija'})


def mitanija(request):
    return render(request, 'senoves_civil/mitanija.html', {'title': 'Mitanija'})


def olmekai(request):
    return render(request, 'senoves_civil/olmekai.html', {'title': 'Olmekai'})


def persija(request):
    return render(request, 'senoves_civil/persija.html', {'title': 'Persija'})


def roma(request):
    return render(request, 'senoves_civil/roma.html', {'title': 'Roma'})


def sangai(request):
    return render(request, 'senoves_civil/sangai.html', {'title': 'Sangai'})


def sia(request):
    return render(request, 'senoves_civil/sia.html', {'title': 'Sia'})


def siognu(request):
    return render(request, 'senoves_civil/siognu.html', {'title': 'Siognu'})


def sirija(request):
    return render(request, 'senoves_civil/sirija.html', {'title': 'Sirija'})


def vedai(request):
    return render(request, 'senoves_civil/vedai.html', {'title': 'Vedai'})


def categories(request, catid):
    return HttpResponse(f"<h1>Kategorijos</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Puslapis nerastas</h1>")
