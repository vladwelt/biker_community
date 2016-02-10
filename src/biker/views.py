from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Evento, Grupo
from .forms import EventoForm, GrupoForm

def groups_list(request):
    groups = Grupo.objects.order_by('nombre')
    return render(request, 'biker/groups_list.html',{'groups':groups})

def events_list(request):
    eventos = Evento.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'biker/events_list.html',{'eventos':eventos})

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
