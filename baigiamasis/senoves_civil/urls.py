
from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('aksumas/', views.aksumas, name='aksumas'),
    path('armenija/', views.armenija, name='armenija'),
    path('asirija/', views.asirija, name='asirija'),
    path('cinai/', views.cinai, name='cinai'),
    path('coment/', views.coment, name='coment'),
    path('dzou/', views.dzou, name='dzou'),
    path('egejas/', views.egejas, name='egejas'),
    path('egiptas/', views.egiptas, name='egiptas'),
    path('elamas/', views.elamas, name='elamas'),
    path('graikija/', views.graikija, name='graikija'),
    path('hanai/', views.hanai, name='hanai'),
    path('home/', views.home, name='home'),
    path('indo_slenis/', views.indo_slenis, name='indo_slenis'),
    path('jamas/', views.jamas, name='jamas'),
    path('jemenas/', views.jemenas, name='jemenas'),
    path('kanaanas/', views.kanaanas, name='kanaanas'),
    path('kusas/', views.kusas, name='kusas'),
    path('libija/', views.libija, name='libija'),
    path('maurja/', views.maurja, name='maurja'),
    path('mazoji_azija/', views.mazoji_azija, name='mazoji_azija'),
    path('mesopotamija/', views.mesopotamija, name='mesopotamija'),
    path('mitanija/', views.mitanija, name='mitanija'),
    path('olmekai/', views.olmekai, name='olmekai'),
    path('persija/', views.persija, name='persija'),
    path('roma/', views.roma, name='roma'),
    path('sangai/', views.sangai, name='sangai'),
    path('sia/', views.sia, name='sia'),
    path('siognu/', views.siognu, name='siognu'),
    path('sirija/', views.sirija, name='sirija'),
    path('vedai/', views.vedai, name='vedai'),


]
