# _*_ coding: utf-8 _*_
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.forms import forms

from .models import Event, Contact,  Foto
from forms import ContactForm

def home(request):
        contatos = Contact.objects.all()
        events = Event.objects.all()
        foto = Foto.objects.all()

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                novo_contato = form.save()
                return HttpResponseRedirect('/thanks/')
        else:
            form = ContactForm()

        return render(request, 'index.html',
                      {
                          'contatos':contatos,
                          'form':form,
                          'events':events,
                          'foto':foto,
                      }
                    )

def event(request, slug):
    event = Event.objects.get(slug=slug)
    return render_to_response('events.html',locals(),
        context_instance=RequestContext(request))

def foto(request, slug):
    foto =  Foto.objects.get(slug=slug)


    return render(request, 'fotos.html',
        {
            'foto':foto,
        }
    )

def album(request):
    foto =  Foto.objects.all()
    paginator = Paginator(foto, 15)
    page = request.GET.get('page')
    try:
        foto = paginator.page(page)
    except PageNotAnInteger:
        foto = paginator.page(1)
    except EmptyPage:
        foto = paginator.page(paginator.num_pages)

    return render(request, 'album.html', {
            'foto':foto,
        }
    )
def thanks(request):

    return render(request, 'thanks.html')
