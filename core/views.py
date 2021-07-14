from core.models import Archivos, ArchivosCapacitacion, ArchivosHitos, Capacitaciones, Duracion, Frecuencia, Gerencia, Hito, HitoAsistencia, Invitados, Tema, Usuarios
from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
import codecs
import datetime

# Create your views here.


def index(request):
    return render(request, 'sitios/index.html')


@login_required(login_url='login')
def buscar(request):
    if request.POST:
        kword = request.POST.get('txtBuscar').strip().replace('  ', '')
        gerencias = Gerencia.objects.filter(nombre_gerencia__icontains=kword)
        temas_gerencia = Tema.objects.filter(
            gerencia__in=gerencias).order_by('-timestamp')
        temas_titulo = Tema.objects.filter(
            nombre__icontains=kword).order_by('-timestamp')
        temas_contenido = Tema.objects.filter(
            contenido__icontains=kword).order_by('-timestamp')
        contexto = {'temas_gerencia': temas_gerencia, 'temas_titulo': temas_titulo,
                    'temas_contenido': temas_contenido, 'kword': kword}
        return render(request, 'sitios/buscar.html', contexto)


@login_required(login_url='login')
def temas(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response
    temas = Tema.objects.all().order_by('-id')
    contexto = {'temas': temas}
    return render(request, 'sitios/temas.html', contexto)


@login_required(login_url='login')
def capacitaciones(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response
    capacitaciones = Capacitaciones.objects.all().order_by('-id')
    contexto = {'capacitaciones': capacitaciones}
    return render(request, 'sitios/capacitaciones.html', contexto)


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
        response = redirect('agregartema')
        return response

    gerencias = Gerencia.objects.all()
    contexto = {'gerencias': gerencias}
    return render(request, 'sitios/agregartema.html', contexto)


@login_required(login_url='login')
def agregarcapacitacion(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if not request.POST:
        frecuencia = Frecuencia.objects.all()
        duracion = Duracion.objects.all()
        temas = Tema.objects.all()
        capacitadores = Usuarios.objects.filter(
            capacitador=True).order_by('user__username')
        contexto = {'frecuencia': frecuencia,
                    'duracion': duracion, 'temas': temas, 'capacitadores': capacitadores}
        return render(request, 'sitios/agregarcapacitacion.html', contexto)
    else:
        # obtener datos POST
        id_capa = request.POST.get('txtIDCapacitacion')
        nombre = request.POST.get('txtNombreCapacitacion')
        id_tema = request.POST.get('cmbTema')
        encargado = request.POST.get('cmbEncargado')
        archivos = request.FILES.getlist('flsArchivos')
        contenido = request.POST.get('txtContenido')
        id_frecuencia = request.POST.get('cmbFrecuencia')
        fecha = request.POST.get('txtFecha')
        fecha_fin = request.POST.get('txtFechaFin')
        hora = request.POST.get('txtHora')
        id_duracion = request.POST.get('cmbDuracion')

        # Obtener FK
        tema = Tema.objects.get(id=id_tema)
        frecuencia = Frecuencia.objects.get(id=id_frecuencia)
        duracion = Duracion.objects.get(id=id_duracion)
        encargado = Usuarios.objects.get(id=encargado)

        # Crear objeto capacitacion
        capacitacion = Capacitaciones()
        if id_capa is not None:
            capacitacion.id = id_capa
            hitos = Hito.objects.filter(capacitacion_id=id_capa)
            hitos.delete()
        capacitacion.tema = tema
        capacitacion.nombre = nombre
        capacitacion.encargado = encargado
        capacitacion.contenido = contenido
        capacitacion.frecuencia = frecuencia
        capacitacion.fecha = fecha
        capacitacion.fecha_fin = fecha_fin
        capacitacion.hora = hora
        capacitacion.duracion = duracion
        capacitacion.save()
        capa = Capacitaciones.objects.all().order_by('-timestamp')[:1]

        start_date = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d").date()
        fecha_hito = start_date
        # fecha_hito = fecha_hito + datetime.timedelta(days=frecuencia.valor)
        continuar = True

        while continuar:
            hito = Hito()
            hito.fecha = fecha_hito
            hito.capacitacion = capa[0]
            hito.save()
            fecha_hito = fecha_hito + datetime.timedelta(days=frecuencia.valor)
            continuar = not (end_date < fecha_hito)

        # while continuar:

        for reg in capa:
            capacitacion = reg
        else:
            for reg in archivos:
                archivo = ArchivosCapacitacion()
                archivo.capacitacion = capacitacion
                archivo.file = reg
                archivo.save()
            else:
                if id_capa is not None:
                    mensaje_exito = f'Capacitación {capacitacion.id} actualizada'
                    messages.success(request, mensaje_exito)
                else:
                    mensaje_exito = f'Capacitación {capacitacion.nombre} creada, id asginado: {capacitacion.id}'
                    messages.success(request, mensaje_exito)
        if id_capa is not None:
            response = redirect('capacitaciones')
            return response

        response = redirect('agregarcapacitacion')
        return response


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
def vercapacitacion(request, id):
    if not request.user.is_staff:
        response = redirect('index')
        return response
    capacitacion = Capacitaciones.objects.get(id=id)
    archivos = ArchivosCapacitacion.objects.filter(capacitacion=capacitacion)
    frecuencia = Frecuencia.objects.all()
    duracion = Duracion.objects.all()
    capacitadores = Usuarios.objects.filter(
        capacitador=True).order_by('user__username')
    temas = Tema.objects.all()
    contexto = {'frecuencia': frecuencia,
                'duracion': duracion,
                'temas': temas,
                'archivos': archivos,
                'capacitacion': capacitacion,
                'capacitadores': capacitadores}
    return render(request, 'sitios/vercapacitacion.html', contexto)


@login_required(login_url='login')
def ver_invitados_hitos(request, id):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    capacitaciones = ArchivosCapacitacion.objects.filter(capacitacion_id=id)
    invitados = Invitados.objects.filter(capacitacion_id=id)
    hitos = Hito.objects.filter(capacitacion_id=id)
    contexto = {'capacitacion': capacitaciones,
                'invitados': invitados,
                'hitos': hitos}
    return render(request, 'sitios/invitadoshitos.html', contexto)


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


@login_required(login_url='login')
def ver_hito(request, id):
    hito = Hito.objects.get(id=id)
    hito_asist = HitoAsistencia.objects.filter(hito_id=hito)
    hito_arch = ArchivosHitos.objects.filter(hito_id=id)
    context = {'hito': hito, 'hito_asist': hito_asist, 'hito_arch': hito_arch}
    return render(request, "sitios/hito.html", context)


@login_required(login_url='login')
def cargar_asistencia(request):
    if request.POST:
        archivo = request.FILES.get('flsArchivo')
        id = request.POST.get('txtIDH')
        file_reader = csv.reader(codecs.iterdecode(
            archivo, 'utf-8'), delimiter=';')
        hito = Hito.objects.get(id=id)
    for row in file_reader:
        hito_asist = HitoAsistencia()
        gerencia = Gerencia.objects.get(id=row[2])
        hito_asist.rut = row[0]
        hito_asist.nombre = row[1]
        hito_asist.gerencia = gerencia
        hito_asist.hito = hito
        hito_asist.save()
    else:
        return redirect('verhito', id=id)


@login_required(login_url='login')
def cargar_anexos(request):
    id = request.POST.get('txtIDH')
    if request.POST:
        archivos = request.FILES.getlist('flsArchivos')
        hito = Hito.objects.get(id=id)
        for reg in archivos:
            ah = ArchivosHitos()
            ah.hito = hito
            ah.file = reg
            ah.save()
        else:
            return redirect('verhito', id=id)
    else:
        return redirect('verhito', id=id)


@login_required(login_url='login')
def cargar_invitados(request):
    if request.POST:
        archivo = request.FILES.get('flsArchivo')
        id = request.POST.get('txtIDC')
        file_reader = csv.reader(codecs.iterdecode(
            archivo, 'utf-8'), delimiter=';')
        capacitacion = Capacitaciones.objects.get(id=id)
    for row in file_reader:
        invitado = Invitados()
        gerencia = Gerencia.objects.get(id=row[2])
        invitado.rut = row[0]
        invitado.nombre = row[1]
        invitado.gerencia = gerencia
        invitado.capacitacion = capacitacion
        invitado.save()
    else:
        return redirect('detalle_capacitacion', id=id)


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
def cerrar_hito(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idHito')
        try:
            hito = Hito.objects.get(id=id)
            hito.estado = True
            hito.save()
            mensaje_exito = f'Se Cerró el Hito {id}'
            messages.success(request, mensaje_exito)
            return HttpResponse("OK")
        except:
            mensaje_error = f'No se pudo actualizar el estado del hito {id}'
            messages.error(request, mensaje_error)
            return HttpResponse("NO")


@csrf_exempt
def eliminar_capa(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idCapa')
        try:
            capa = Capacitaciones.objects.get(id=id)
            capa.delete()
            mensaje_exito = f'Se eliminó la capacitación {id}'
            messages.success(request, mensaje_exito)
            return HttpResponse("OK")
        except:
            mensaje_error = f'No se pudo eliminar la capacitación número {id}'
            messages.error(request, mensaje_error)
            return HttpResponse("NO")


@csrf_exempt
def eliminar_hito(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idHito')
        try:
            hito = Hito.objects.get(id=id)
            hito.delete()
            mensaje_exito = f'Se eliminó el Hito {id}'
            messages.success(request, mensaje_exito)
            return HttpResponse("OK")
        except:
            mensaje_error = f'No se pudo eliminar el Hito número {id}'
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


@csrf_exempt
def eliminar_adjunto_hito(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idArchivo')
        try:
            archivo = ArchivosHitos.objects.get(id=id)
            archivo.delete()
            return HttpResponse("OK")
        except:
            return HttpResponse("NO")


@csrf_exempt
def eliminar_adjunto_capacitacion(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idArchivo')
        try:
            archivo = ArchivosCapacitacion.objects.get(id=id)
            archivo.delete()
            return HttpResponse("OK")
        except:
            return HttpResponse("NO")


@csrf_exempt
def eliminar_invitado_capacitacion(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idInvitado')
        try:
            invitado = Invitados.objects.get(id=id)
            invitado.delete()
            return HttpResponse("OK")
        except:
            return HttpResponse("NO")
        

@csrf_exempt
def eliminar_asistente(request):
    if not request.user.is_staff:
        response = redirect('index')
        return response

    if request.POST:
        id = request.POST.get('idAsistencia')
        try:
            asistente = HitoAsistencia.objects.get(id=id)
            asistente.delete()
            return HttpResponse("OK")
        except:
            return HttpResponse("NO")