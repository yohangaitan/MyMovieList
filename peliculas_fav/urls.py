"""
URL configuration for peliculas_fav project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views                     #importaciones importantes para el funcionamiento
from django.conf import settings
from django.conf.urls.static import static


#todas las url utilizadas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name='inicio'),
    path('registrarse/',views.registrarse, name='registrarse'),
    path('peliculas/',views.peliculas, name='peliculas'),
    path('peliculas/create/',views.agg_pelicula, name='agg_pelicula'),
    path('peliculas/<int:pelicula_id>/',views.detalles_pelicula, name='detalles_pelicula'),
    path('peliculas/<int:pelicula_id>/borrar',views.borrar_pelicula, name='borrar_pelicula'),
    path('contactanos/',views.contactanos, name='contactanos'),
    path('favoritas/',views.favoritas, name='favoritas'),
    path('cerrarsesion/',views.cerrarsesion, name='cerrarsesion'),
    path('iniciarsesion/',views.iniciarsesion, name='iniciarsesion'),
    path('marcar_favorita/<int:pelicula_id>/', views.marcar_favorita, name='marcar_favorita'),
    
    
]
#para que se pudiese subir la imagen de las peliculas
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)