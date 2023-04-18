
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
