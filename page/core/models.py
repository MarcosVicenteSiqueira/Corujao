# _*_ coding: utf-8 _*_

from django.core.urlresolvers import reverse
# Create your models here.
from django.db import models
from photologue.models import Gallery
from taggit.managers import TaggableManager


class Event(models.Model):
    class Meta:
        ordering = ('-data',)

    titulo = models.CharField(max_length=50)
    data = models.DateTimeField('date published')
    imagem = models.ImageField(upload_to='event/')
    galeria = models.OneToOneField('Galeria')
    text = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)


    def get_absolute_url(self):
        return reverse('core.views.event',(), kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo

class GalleryExtended(models.Model):
    gallery = models.OneToOneField(Gallery, related_name='extended')
    tags = TaggableManager(blank=True)


    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __unicode__(self):
        return self.gallery.title

class Galeria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    foto = models.ManyToManyField('Foto')

    def get_absolute_url(self):
        return reverse('core.views.galeria',(), kwargs={'slug': self.slug})
    def __unicode__(self):
        return self.nome

class Foto(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    imagem = models.ImageField(upload_to='foto/')
    descricao = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('core.views.foto',(), kwargs={'slug': self.slug})

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

class Comment(models.Model):
    name_comment = models.CharField(max_length=100)
    data_comment = models.DateField('data published')
    email = models.URLField(max_length=200)
    cometario = models.TextField()


    def __unicode__(self):
        return self.name_comment
