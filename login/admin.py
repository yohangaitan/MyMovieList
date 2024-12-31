from django.contrib import admin
from .models import Peliculas

class PeliculasAdmin(admin.ModelAdmin):
    readonly_fields = ("guardado", )

# Register your models here.
admin.site.register(Peliculas, PeliculasAdmin)