from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Evento, Grupo, Ruta, Usuario
from .forms import EventoForm, GrupoForm, RutaForm

def routes_list(request):
    routes = Ruta.objects.order_by('nombre')
    return render(request, 'biker/routes_list.html',{'routes':routes})

def groups_list(request):
    groups = Grupo.objects.order_by('nombre')
    return render(request, 'biker/groups_list.html',{'groups':groups})

def group_detail(request, pk):
    grupo = get_object_or_404(Grupo,pk=pk)
    usuarios = Usuario.objects.filter(grupo_id=pk)
    return render(request, 'biker/group_detail.html',{'grupo': grupo,'usuario':usuarios})

def route_detail(request, pk):
    ruta = get_object_or_404(Ruta,pk=pk)
    return render(request, 'biker/route_detail.html',{'ruta': ruta})

def events_list(request):
    eventos = Evento.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'biker/events_list.html',{'eventos':eventos})

def delete_ruta(request,pk):
    ruta = get_object_or_404(Ruta,pk=pk)
    ruta.delete()
    return HttpResponseRedirect('/rutas/')

def delete_evento(request,pk):
    evento = get_object_or_404(Evento,pk=pk)
    evento.delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def delete_group(request,pk):
    grupo = get_object_or_404(Grupo,pk=pk)
    grupo.delete()
    return HttpResponseRedirect('/grupos/')

@login_required(login_url='/login/')
def event_detail(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    grupos = evento.grupo.all()
    return render(request, 'biker/event_detail.html',{ 'evento': evento, 'grupos': grupos })

@login_required(login_url='/login/')
def registrar_evento(request):
    if request.method == 'POST':
        try:
            eventoForm = EventoForm(request.POST, request.FILES)
            if eventoForm.is_valid():
                evento_nuevo = eventoForm.save()
                return HttpResponseRedirect('/')
        except Exception as e:
            print("ERROR AL REGISTRAR EL EVENTO ", e)
    else:
        eventoForm = EventoForm()
    return render(request, 'biker/registrar_evento.html', {'form': eventoForm})

@login_required(login_url='/login/')
def registrar_grupo(request):
    if request.method == 'POST':
        try:
            grupoForm = GrupoForm(request.POST, request.FILES)
            if grupoForm.is_valid():
                grupo_nuevo = grupoForm.save()
                return HttpResponseRedirect('/grupos')
        except Exception as e:
            print("ERROR AL REGISTRAR EL GRUPO ", e)
    else:
        grupoForm = GrupoForm()
    return render(request, 'biker/registrar_grupo.html', {'form': grupoForm})

@login_required(login_url='/login/')
def registrar_ruta(request):
    if request.method == 'POST':
        try:
            rutaForm = RutaForm(request.POST, request.FILES)
            if rutaForm.is_valid():
                ruta_nueva = rutaForm.save()
                return HttpResponseRedirect('/rutas')
        except Exception as e:
            print("ERROR AL REGISTRAR EL RUTA ", e)
    else:
        rutaForm = RutaForm()
    return render(request, 'biker/registrar_ruta.html', {'form': rutaForm})

@login_required(login_url='/login/')
def event_edit(request, pk):
    evento_nuevo=get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        try:
            eventoForm = EventoForm(request.POST, request.FILES, instance=evento_nuevo)
            if eventoForm.is_valid():
                eventoForm.save()
                return HttpResponseRedirect('/')
        except Exception as e:
            print("ERROR AL EDITAR EL EVENTO ", e)
    else:
        eventoForm = EventoForm(instance=evento_nuevo)
    return render(request, 'biker/editar_evento.html', {'form': eventoForm})


@login_required(login_url='/login/')
def group_edit(request, pk):
    grupo_nuevo=get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        try:
            grupoForm = GrupoForm(request.POST, request.FILES, instance=grupo_nuevo)
            if grupoForm.is_valid():
                grupo_nuevo = grupoForm.save()
                return HttpResponseRedirect('/grupos')
        except Exception as e:
            print("ERROR AL REGISTRAR EL GRUPO ", e)
    else:
        grupoForm = GrupoForm(instance=grupo_nuevo)
    return render(request, 'biker/editar_grupo.html', {'form': grupoForm})

@login_required(login_url='/login/')
def route_edit(request, pk):
    ruta_nueva=get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        try:
            rutaForm = RutaForm(request.POST, request.FILES, instance=ruta_nueva)
            if rutaForm.is_valid():
                ruta_nueva = rutaForm.save()
                return HttpResponseRedirect('/rutas')
        except Exception as e:
            print("ERROR AL REGISTRAR EL RUTA ", e)
    else:
        rutaForm = RutaForm(instance=ruta_nueva)
    return render(request, 'biker/editar_ruta.html', {'form': rutaForm})

