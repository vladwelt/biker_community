from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Evento

def group_list(request):
    eventos = Evento.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'biker/group_list.html',{'eventos':eventos})

def event_detail(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'biker/event_detail.html',{'evento': evento})
# Create your views here.
