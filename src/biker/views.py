from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .models import Evento, Grupo, Ruta, Usuario
from .forms import EventoForm, GrupoForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

def index(request):
    eventos = Evento.objects.filter(fecha__lte=timezone.now()).order_by('fecha')[:3]
    routes = Ruta.objects.order_by('nombre')[:3]
    groups = Grupo.objects.order_by('nombre')[:3]
    return render(request, 'biker/index.html',
            {'eventos':eventos,
             'rutas':routes,
             'grupos': groups})

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

class RutaCreate(CreateView):
    model = Ruta
    fields = ['nombre','distancia','descripcion','imagen']
    template_name = 'biker/ruta_create_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RutaCreate, self).form_valid(form)

class RutaDetail(DetailView):

    model = Ruta

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RutaDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context

class RutaListView(ListView):
    model = Ruta

    def get_context_data(self, **kwargs):
        context = super(RutaListView, self).get_context_data(**kwargs)
        return context

class RutaDelete(DeleteView):
    model = Ruta
    success_url = reverse_lazy('ruta-list')

class RutaUpdate(UpdateView):
    model = Ruta
    fields = ['nombre', 'distancia', 'descripcion', 'imagen']
    template_name_suffix = '_update_form'
