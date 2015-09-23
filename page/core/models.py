# _*_ coding: utf-8 _*_

from django.core.urlresolvers import reverse
# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _




class Event(models.Model):
    class Meta:
        ordering = ('-data',)

    titulo = models.CharField(max_length=50)
    data = models.DateTimeField('date published')
    imagem = models.ImageField(upload_to='event/')
    text = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)


    def get_absolute_url(self):
        return reverse('core.views.event',(), kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo

class Foto(models.Model):
    class Meta:
        ordering = ('-name',)
    name = models.CharField(_('Nome'),max_length=200)
    slug = models.SlugField(unique=True)
    data = models.DateTimeField(auto_now_add = True)
    imagem = models.ImageField(upload_to='foto/')
    descricao = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    nome = models.CharField(max_length=100)
    endereco  = models.CharField(max_length=100)
    numero_endereco = models.CharField(max_length=5)
    dd_telefone = models.CharField(max_length=2)
    numero_telefone = models.CharField(max_length=8)
    email = models.URLField(max_length=200)
    texto = models.TextField()

    def  __unicode__(self):
        return self.nome
