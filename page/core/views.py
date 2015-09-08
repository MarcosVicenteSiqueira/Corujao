# _*_ coding: utf-8 _*_
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.forms import forms

from .models import Event, Contact, Comment, Foto, Galeria
from forms import ContactForm, CommentForms

def home(request):
        contatos = Contact.objects.all()
        events = Event.objects.all()
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
                      }
                    )

def comment(request):
    comment = Comment.objects.all()
    if request.method =="POST":
        form_comment = CommentForms(request.POST)
        if form_comment.is_valid():
            novo_comment = form_comment.save()
            return HttpResponseRedirect(reverse('events'))
    else:
        form_comment = CommentForms()

    return render(request, 'comment.html',
                  {
                    'comment':comment,
                    'form_comment':form_comment,
                }
            )

def event(request, slug):
    event = Event.objects.get(slug=slug)
    comment = Comment.objects.all()
    return render_to_response('events.html',locals(),
        context_instance=RequestContext(request))

def foto(request, slug):
    foto =  Foto.objects.get(slug=slug)
    return render(request, 'fotos.html',
    { 'foto':foto,}
    )

def album(request, slug):
    album =  Galeria.objects.all()
    return render(request, 'album.html',{'album':album})

def thanks(request):
    return render(request, 'thanks.html')
