from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .models import Evento, Grupo, Ruta, Usuario
from .forms import EventoForm
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
        context = super(RutaDetail, self).get_context_data(**kwargs)
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

class GrupoCreate(CreateView):
    model = Grupo
    fields = ['nombre','descripcion','imagen']
    template_name = 'biker/grupo_create_form.html'

    def form_valid(self, form):
        form.instance.administrador = Usuario.objects.get(user=self.request.user)
        return super(GrupoCreate, self).form_valid(form)

class GrupoDetail(DetailView):
    model = Grupo

    def get_context_data(self, **kwargs):
        context = super(GrupoDetail, self).get_context_data(**kwargs)
        return context

class GrupoListView(ListView):
    model = Grupo

    def get_context_data(self, **kwargs):
        context = super(GrupoListView, self).get_context_data(**kwargs)
        return context

class GrupoDelete(DeleteView):
    model = Grupo
    success_url = reverse_lazy('group-list')

class GrupoUpdate(UpdateView):
    model = Grupo
    fields = ['nombre', 'descripcion', 'imagen']
    template_name_suffix = '_update_form'

class EventoCreate(CreateView):
    model = Evento
    fields = ['nombre','punto_partida','descripcion','fecha','ruta','grupo','imagen']
    template_name = 'biker/evento_create_form.html'

    def form_valid(self, form):
        form.instance.administrador = Usuario.objects.get(user=self.request.user)
        return super(EventoCreate, self).form_valid(form)

class EventoDetail(DetailView):
    model = Evento

    def get_context_data(self, **kwargs):
        context = super(EventoDetail, self).get_context_data(**kwargs)
        return context

class EventoListView(ListView):
    model = Evento

    def get_context_data(self, **kwargs):
        context = super(EventoListView, self).get_context_data(**kwargs)
        return context

class EventoDelete(DeleteView):
    model = Evento
    success_url = reverse_lazy('group-list')

class EventoUpdate(UpdateView):
    model = Evento
    fields = ['nombre','punto_partida','descripcion','fecha','ruta','grupo','imagen']
    template_name_suffix = '_update_form'
