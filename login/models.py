from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Peliculas(models.Model):                                      #la base de datos
    titulo = models.CharField(max_length=100)
    reseña = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)
    guardado = models.DateTimeField(auto_now_add=True)
    favorita = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo + '- por ' + self.user.username
    
    class Meta:
        db_table = "Peliculas"