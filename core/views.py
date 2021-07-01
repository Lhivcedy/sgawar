from core.models import Archivos, Tema
from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'sitios/index.html')


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
        tema = Tema()
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

        return render(request, 'sitios/agregartema.html')
    else:
        return render(request, 'sitios/agregartema.html')


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


@csrf_exempt
def ajaxtest(request):
    if request.POST:
        test = request.POST.get('user')
        return HttpResponse(test)
    else:
        return HttpResponse('xd')
