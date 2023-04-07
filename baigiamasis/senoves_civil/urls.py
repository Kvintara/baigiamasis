
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('aksumas/', aksumas, name='aksumas'),
    path('armenija/', armenija, name='armenija'),
    path('asirija/', asirija, name='asirija'),
    path('cinai/', cinai, name='cinai'),
    path('coment/', coment, name='coment'),
    path('dzou/', dzou, name='dzou'),
    path('egejas/', egejas, name='egejas'),
    path('egiptas/', egiptas, name='egiptas'),
    path('elamas/', elamas, name='elamas'),
    path('graikija/', graikija, name='graikija'),
    path('hanai/', hanai, name='hanai'),
    path('home/', home, name='home'),
    path('indo_slenis/', indo_slenis, name='indo_slenis'),
    path('jamas/', jamas, name='jamas'),
    path('jemenas/', jemenas, name='jemenas'),
    path('kanaanas/', kanaanas, name='kanaanas'),
    path('kusas/', kusas, name='kusas'),
    path('libija/', libija, name='libija'),
    path('maurja/', maurja, name='maurja'),
    path('mazoji_azija/', mazoji_azija, name='mazoji_azija'),
    path('mesopotamija/', mesopotamija, name='mesopotamija'),
    path('mitanija/', mitanija, name='mitanija'),
    path('olmekai/', olmekai, name='olmekai'),
    path('persija/', persija, name='persija'),
    path('roma/', roma, name='roma'),
    path('sangai/', sangai, name='sangai'),
    path('sia/', sia, name='sia'),
    path('siognu/', siognu, name='siognu'),
    path('sirija/', sirija, name='sirija'),
    path('vedai/', vedai, name='vedai'),


]
