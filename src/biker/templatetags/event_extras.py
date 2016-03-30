from django import template
from biker.models import Usuario, Evento

register = template.Library()

@register.filter(name='is_in_group')
def is_in_group(user, event_id):
    user_logged = Usuario.objects.get(user=user.id)
    event = Evento.objects.get(id=event_id)
    return event.participantes.filter(user_id=user_logged.pk).exists()
