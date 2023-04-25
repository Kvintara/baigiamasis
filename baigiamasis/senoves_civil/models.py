
from django.db import models

# Create models here.


class Civilizacijos(models.Model):
    title = models.CharField(max_length=100)
    region = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Senoves Civilizacijos'
        verbose_name_plural = 'Civilizacijos'


# *------------------coment------------------

class Coment(models.Model):
    nick = models.CharField('Nikas', max_length=50)
    title = models.CharField('Komentaro pavadinimas', max_length=100)
    content = models.TextField('Komentaras')
    date = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Komentaras'
        verbose_name_plural = 'Komentarai'

# *-------------Register, login, logout----------------
