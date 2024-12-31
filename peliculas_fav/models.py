from django.db import models

class Peliculas(models.Model):
    titulo = models.CharField(max_length=150)
    director = models.CharField(max_length=50)
    anio = models.IntegerField()
    genero = models.CharField(max_length=50)

class Actores(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)

class PeliculasActores(models.Model): #esto seria la tabla pivote
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actores, on_delete=models.CASCADE)