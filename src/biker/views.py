from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, JsonResponse
from django.template import Context, RequestContext
from django.core.urlresolvers import reverse_lazy
from .forms import RutaForm, EventoSearchForm, RutaSearchForm, GrupoSearchForm, SolicitudForm
from .models import Evento, Grupo, Ruta, Usuario, Solicitud
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from django.views.generic.list import ListView

def index(request):
    eventos = reversed(Evento.objects.order_by('fecha'))
    routes = Ruta.objects.order_by('nombre')
    groups = Grupo.objects.order_by('nombre')
    return render(request, 'biker/index.html',
            {'eventos':eventos,
             'rutas':routes,
             'grupos': groups})

def login_index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if request.is_ajax:
                user = login(request, user)
                if user is not None:
                    return HttpResponse('/')
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseForbidden() # catch invalid ajax and all non ajax
    return render_to_response('registration/login.html', context_instance=RequestContext(request))

def search_event(request):
    if request.method =='POST':
        form=EventoSearchForm(request.POST)
        if form.is_valid():
            nombre_evento=form.cleaned_data['nombre_evento']
            eventos=Evento.objects.filter(nombre__contains=nombre_evento)
        return render(request,'biker/search_event.html',{'eventos':eventos})
    else:
        form=EventoSearchForm()
    return render(request,'biker/search_event_form.html',{'form':form})

def search_group(request):
    if request.method =='POST':
        form=GrupoSearchForm(request.POST)
        if form.is_valid():
            nombre_grupo=form.cleaned_data['nombre_grupo']
            grupos=Grupo.objects.filter(nombre__contains=nombre_grupo)
        return render(request,'biker/search_group.html',{'grupos':grupos})
    else:
        form=GrupoSearchForm()
    return render(request,'biker/search_group_form.html',{'form':form})

def search_route(request):
    if request.method =='POST':
        form=RutaSearchForm(request.POST)
        if form.is_valid():
            nombre_ruta=form.cleaned_data['nombre_ruta']
            rutas=Ruta.objects.filter(nombre__contains=nombre_ruta)
        return render(request,'biker/search_route.html',{'rutas':rutas})
    else:
        form=RutaSearchForm()
    return render(request,'biker/search_route_form.html',{'form':form})

class RutaCreate(CreateView):
    template_name = 'biker/ruta_create_form.html'
    form_class = RutaForm

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
        if self.request.user.is_authenticated():
            group = self.get_object()

            user = Usuario.objects.get(pk=self.request.user)
            is_admin = group.administrador.pk == self.request.user.pk
            solicitude = Solicitud.objects.filter(user=self.request.user.pk, group=group)
            context['is_admin'] = is_admin

            if solicitude:
                print(solicitude)
                context['solicitude_state'] = solicitude[0].state
        return context

class GrupoListView(ListView):
    model = Grupo

    def get_context_data(self, **kwargs):
        context = super(GrupoListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            my_groups = Usuario.objects.get(pk=self.request.user).grupo_set.all()
            groups_solicitudes = []
            for group in my_groups:
                groups_solicitudes.append([group, Solicitud.objects.filter(group=group)])
            context['my_groups'] = groups_solicitudes
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
    success_url = reverse_lazy('event-list')

class EventoUpdate(UpdateView):
    model = Evento
    fields = ['nombre','punto_partida','descripcion','fecha','ruta','grupo','imagen']
    template_name_suffix = '_update_form'

def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitude = form.save(commit=False)
            user = Usuario.objects.get(pk=request.user.id)
            solicitude.user = user
            solicitude.save()
    return  HttpResponseRedirect('/group/list')

def solicitud_accept(request):
    if request.method == 'POST':
        solicitude_id = request.POST['solicitude']
        solicitud = Solicitud.objects.get(id=solicitude_id)
        if request.user == solicitud.group.administrador.user:
            solicitud.accepted()
    return  HttpResponse('/group/list')

def join_event(request):
    if request.method == 'POST':
        event_id = request.POST['event']
        if request.is_ajax:
            event = Evento.objects.get(id=event_id)
            usuario = Usuario.objects.get(user = request.user)
            event.participantes.add(usuario)
            return JsonResponse({'status': 'true'})
        return HttpResponseForbidden() # catch invalid ajax and all non ajax

