from django.utils import timezone
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
def events_list(request):
    eventos = Evento.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'biker/events_list.html',{'eventos':eventos})
def delete_group(request,pk):
    grupo = get_object_or_404(Grupo,pk=pk)
    grupo.delete()
    return HttpResponseRedirect('/grupos/')

def group_detail(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    users = Usuario.objects.filter(grupo=grupo.id)
    events = Evento.objects.filter(grupo=grupo.id)
    return render(request, 'biker/group_detail.html',{ 'users': users, 'eventos': events, 'grupo': grupo })

def event_detail(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    grupos = evento.grupo.all()
    return render(request, 'biker/event_detail.html',{ 'evento': evento, 'grupos': grupos })
def registrar_evento(request):
    if request.method == 'POST':
        try:
            eventoForm = EventoForm(request.POST)
            if eventoForm.is_valid():
                evento_nuevo = eventoForm.save()
                return HttpResponseRedirect('/registrar/evento')
        except Exception as e:
            print("ERROR AL REGISTRAR EL EVENTO ", e)
    else:
        eventoForm = EventoForm()
    return render(request, 'biker/registrar_evento.html', {'form': eventoForm})

def registrar_grupo(request):
    if request.method == 'POST':
        try:
            grupoForm = GrupoForm(request.POST)
            if grupoForm.is_valid():
                grupo_nuevo = grupoForm.save()
                return HttpResponseRedirect('/registrar/grupo')
        except Exception as e:
            print("ERROR AL REGISTRAR EL GRUPO ", e)
    else:
        grupoForm = GrupoForm()
    return render(request, 'biker/registrar_grupo.html', {'form': grupoForm})

def registrar_ruta(request):
    if request.method == 'POST':
        try:
            rutaForm = RutaForm(request.POST)
            if rutaForm.is_valid():
                ruta_nueva = rutaForm.save()
                return HttpResponseRedirect('/registrar/ruta')
        except Exception as e:
            print("ERROR AL REGISTRAR EL RUTA ", e)
    else:
        rutaForm = RutaForm()
    return render(request, 'biker/registrar_ruta.html', {'form': rutaForm})

def event_edit(request, pk):
    evento_nuevo=get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        try:
            eventoForm = EventoForm(request.POST, instance=evento_nuevo)
            if eventoForm.is_valid():
                eventoForm.save()
                return HttpResponseRedirect('/')
        except Exception as e:
            print("ERROR AL EDITAR EL EVENTO ", e)
    else:
        eventoForm = EventoForm(instance=evento_nuevo)
    return render(request, 'biker/editar_evento.html', {'form': eventoForm})


def group_edit(request, pk):
    grupo_nuevo=get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        try:
            grupoForm = GrupoForm(request.POST, instance=grupo_nuevo)
            if grupoForm.is_valid():
                grupo_nuevo = grupoForm.save()
                return HttpResponseRedirect('/registrar/grupo')
        except Exception as e:
            print("ERROR AL REGISTRAR EL GRUPO ", e)
    else:
        grupoForm = GrupoForm(instance=grupo_nuevo)
    return render(request, 'biker/editar_grupo.html', {'form': grupoForm})

def route_edit(request, pk):
    ruta_nueva=get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        try:
            rutaForm = RutaForm(request.POST, instance=ruta_nueva)
            if rutaForm.is_valid():
                ruta_nueva = rutaForm.save()
                return HttpResponseRedirect('/registrar/ruta')
        except Exception as e:
            print("ERROR AL REGISTRAR EL RUTA ", e)
    else:
        rutaForm = RutaForm(instance=ruta_nueva)
    return render(request, 'biker/editar_ruta.html', {'form': rutaForm})

