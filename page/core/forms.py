# _*_ coding: utf-8 _*_
from django import forms

from .models import Contact

class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    dd_telefone = forms.CharField(label='dd',max_length=2)
    numero_telefone = forms.CharField(label='Telefone',max_length=8)
    email = forms.EmailField(label='Email',max_length=200)
    texto = forms.CharField(widget=forms.Textarea)

    def save(self, contato=None):
        nome = self.cleaned_data.get('nome')
        dd_telefone = self.cleaned_data.get('dd_telefone')
        numero_telefone = self.cleaned_data.get('numero_telefone')
        email = self.cleaned_data.get('email')
        texto = self.cleaned_data.get('texto')

        if contato:
            contato.nome = nome
            contato.dd_telefone = dd_telefone
            contato.numero_telefone = numero_telefone
            contato.email = email
            contato.texto = texto
        else:
            novo_contato = Contact(
                nome= nome,
                dd_telefone = dd_telefone,
                numero_telefone = numero_telefone,
                email = email,
                texto = texto
            )

        novo_contato.save()
        return novo_contato
