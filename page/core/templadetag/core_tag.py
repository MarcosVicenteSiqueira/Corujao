from django import template
from core import models

register = template.Library()
@register.inclusion_tag('fotos.html')
def display_fotos(fotos_id):
    fotos = models.Fotos.objects.get(id_exact=fotos_id)
    return {'fotos':fotos}