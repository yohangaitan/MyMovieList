from django.shortcuts import render, redirect, get_object_or_404 #para que al visitar una pagina inexistente marque otro tipo de error de menos vulnerabilidad
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate #para funciones del login
from django.db import IntegrityError
from .forms import peliculaForm
from .models import Peliculas #importa el modelo Peliculas
from django.utils import timezone #importa esta funcion de Django, de hecho no se usa en este proyecto
from django.contrib.auth.decorators import login_required #importacion para seguridad

# Create your views here.

    # para la vista web peliculas
@login_required
def peliculas(request):
    peliculas = Peliculas.objects.filter(user=request.user)
    return render(request, 'peliculas.html', {'peliculas': peliculas})

    #para visra web de agregar una pelicula
@login_required
def agg_pelicula(request):
    if request.method == 'GET':
        return render(request, 'agg_peliculas.html', {
            'form': peliculaForm
        })
    else:
        try:
            form = peliculaForm(request.POST, request.FILES)
            new_pelicula = form.save(commit=False)
            new_pelicula.user = request.user
            new_pelicula.save() #generará un dato dentro de la base de datos
            return redirect('peliculas')
        except ValueError:
            return render (render, 'agg_peliculas.html', {
                'form': peliculaForm,
                'error': 'por favor proporciona datos válidos'
            })
            
    #para cuando entres a una pelicula y la quieras editar como borrar o actualizar
@login_required
def detalles_pelicula(request, pelicula_id):
    if request.method == 'GET':
        pelicula = get_object_or_404(Peliculas, pk=pelicula_id, user=request.user)
        form = peliculaForm(instance=pelicula)
        return render(request, 'detalles_pelicula.html', {'pelicula': pelicula, 'form': form})
    else:
        try:
            pelicula = get_object_or_404(Peliculas, pk=pelicula_id, user=request.user)
            form = peliculaForm(request.POST, instance=pelicula)
            form.save()
            return redirect('peliculas')
        except ValueError: #una excepcion de un error por si llegase a suceder
            return render(request, 'detalles_pelicula.html', {'pelicula': pelicula, 'form': form,
            'error': "Error actualizando peliculas"}) #mostraria este mensaje

    #para borrar una pelicula
def borrar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Peliculas, pk=pelicula_id, user=request.user)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('peliculas')

    #funcion para el inicio que retorne a inicio
def inicio(request):
    return render(request, 'inicio.html')

    #la funcion para registrarse
def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('peliculas')
            except IntegrityError:
                return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    "error": 'El nombre de usuario ya existe'
                })
        return render(request, 'registrarse.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })

    
    return render(request, 'peliculas.html', {'peliculas':peliculas})

    #la funcion para que la pagina de contactanos se muestre
def contactanos(request):
    return render(request, 'contactanos.html')


@login_required
def favoritas(request):
    return render(request, 'favoritas.html')

    #la funcion de cerrar sesion
@login_required
def cerrarsesion(request):
    logout(request)
    return redirect('inicio')

    #la de iniciar sesion luego de haberse registrado
def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarsesion.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'iniciarsesion.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña es incorrecto' #mensaje si la contraseña o usuario no coinciden
            })
        else:
            login(request, usuario)
            return redirect('peliculas')
            
        return render(request, 'iniciarsesion.html', {
            'form': AuthenticationForm
        })

#funcion para marcar pelicula en favoritos 
def marcar_favorita(request, pelicula_id):
        pelicula = get_object_or_404(Peliculas, id=pelicula_id)
        pelicula.favorita = not pelicula.favorita
        pelicula.save()
        return redirect('peliculas')
