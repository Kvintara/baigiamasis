
from django.urls import path
from .views import *


urlpatterns = [
    # http://127.0.0.1:8000/senoves_civil/
    path('', index),
    # http://127.0.0.1:8000/senoves_civil/categ/1/
    path('categ/<int:catid>/', categories),
]
