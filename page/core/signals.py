from django.db.models import signals
from django.template.defaultfilters import slugify
from .models import Event


def artigo_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    artigo com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade"""
    if not instance.slug:
        slug = slugify(instance.titulo)
        novo_slug = slug
        contador = 0

        while Event.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug

signals.pre_save.connect(artigo_pre_save, sender=Event)
