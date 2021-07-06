from core.models import Archivos, Gerencia, Tema
from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'sitios/index.html')

@login_required(login_url='login')
def buscar(request):
    if request.POST:
        kword = request.POST.get('txtBuscar').strip().replace('  ', '')
        gerencias = Gerencia.objects.filter(nombre_gerencia__icontains=kword)
        temas_gerencia = Tema.objects.filter(gerencia__in = gerencias).order_by('-timestamp')
        temas_titulo = Tema.objects.filter(nombre__icontains = kword).order_by('-timestamp')
        temas_contenido = Tema.objects.filter(contenido__icontains = kword).order_by('-timestamp')
        contexto = {'temas_gerencia': temas_gerencia, 'temas_titulo': temas_titulo, 'temas_contenido':temas_contenido, 'kword':kword}
        return render(request, 'sitios/buscar.html', contexto)
        

@login_required(login_url='login')
def temas(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response
    temas = Tema.objects.all().order_by('-timestamp')
    contexto = {'temas': temas}
    return render(request, 'sitios/temas.html', contexto)


@login_required(login_url='login')
def agregartema(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        user = request.user
        nombre = request.POST.get('txtNombreTema')
        contenido = request.POST.get('txtContenido')
        archivos = request.FILES.getlist('flsArchivos')
        id_gerencia = request.POST.get('cmbGerencia')
        print(id_gerencia)
        gerencia = Gerencia.objects.get(id=id_gerencia)
        tema = Tema()
        tema.gerencia = gerencia
        tema.nombre = nombre
        tema.contenido = contenido
        tema.autor = user
        tema.save()
        temas = Tema.objects.all().order_by('-timestamp')[:1]
        for reg in temas:
            tema = reg
        else:
            for reg in archivos:
                archivo = Archivos()
                archivo.file = reg
                archivo.tema = tema
                archivo.save()
            else:
                mensaje_exito = f'Tema {tema.nombre} creado, id asginado: {tema.id}'
                messages.success(request, mensaje_exito)

    gerencias = Gerencia.objects.all()
    contexto = {'gerencias': gerencias}
    return render(request, 'sitios/agregartema.html', contexto)


@login_required(login_url='login')
def actualizartema(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response
    if request.POST:
        id_tema = request.POST.get('txtIDTema')
        id_gerencia = request.POST.get('cmbGerencia')
    try:
        tema = Tema.objects.get(id=id_tema)
        gerencia = Gerencia.objects.get(id=id_gerencia)
        tema.nombre = request.POST.get('txtNombreTema')
        tema.contenido = request.POST.get('txtContenido')
        tema.gerencia = gerencia
        archivos_form = request.FILES.getlist('flsArchivos')
        tema.save()
        for reg in archivos_form:
            archivo = Archivos()
            archivo.file = reg
            archivo.tema = tema
            archivo.save()
        mensaje_exito = f'Se actualizó el tema {tema.id}'
        messages.success(request, mensaje_exito)
    except:
        mensaje_error = f'No se pudo actualizar el tema número {tema.id}'
        messages.error(request, mensaje_error)
    response = redirect('temas')
    return response


@login_required(login_url='login')
def vertema(request, id):
    if not request.user.is_staff:
        response = redirect('index')
        return response
    tema = Tema.objects.get(id=id)
    archivos = Archivos.objects.filter(tema=tema)
    gerencias = Gerencia.objects.all()
    contexto = {'tema': tema, 'archivos': archivos, 'gerencias': gerencias}
    return render(request, 'sitios/vertema.html', contexto)


@login_required(login_url='login')
def cerrar(request):
    logout(request)
    return render(request, "sitios/index.html")


def login(request):
    if request.user.is_authenticated:
        response = redirect('index')
        return response

    if request.POST:
        usuario = request.POST.get('txtUsuario')
        pwd = request.POST.get('txtPassword')
        us = authenticate(request, username=usuario, password=pwd)
        if us is not None and us.is_active:
            response = redirect('index')
            login_aut(request, us)
            return response
        else:
            mensaje = 'Error'
            contexto = {'mensaje': mensaje}
            return render(request, 'sitios/login.html', contexto)

    return render(request, 'sitios/login.html')

# Metodos AJAX


@csrf_exempt
def eliminar_tema(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idTema')
        try:
            tema = Tema.objects.get(id=id)
            tema.delete()
            mensaje_exito = f'Se eliminó el tema {id}'
            messages.success(request, mensaje_exito)
            return HttpResponse("OK")
        except:
            mensaje_error = f'No se pudo eliminar el tema número {tema.id}'
            messages.error(request, mensaje_error)
            return HttpResponse("NO")


@csrf_exempt
def eliminar_adjunto(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idArchivo')
        try:
            archivo = Archivos.objects.get(id=id)
            archivo.delete()
            return HttpResponse("OK")
        except:
            return HttpResponse("NO")
