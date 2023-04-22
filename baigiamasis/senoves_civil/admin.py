
from django.contrib import admin
from .models import *

# Register your models here.


class CivilizacijosAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'content', 'image')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'region')
    list_filter = ('title', 'content', 'region')


admin.site.register(Civilizacijos, CivilizacijosAdmin)

# *------------------coment------------------


class ComentAdmin(admin.ModelAdmin):
    list_display = ('nick', 'title', 'content', 'date')
    list_display_links = ('nick', 'title', 'content', 'date')
    search_fields = ('nick', 'title', 'content', 'date')
    list_filter = ('nick', 'title', 'content', 'date')


admin.site.register(Coment, ComentAdmin)
