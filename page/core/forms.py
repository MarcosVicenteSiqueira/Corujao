# _*_ coding: utf-8 _*_
from django import forms

from .models import Contact, Comment
    
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

class CommentForms(forms.Form):

    name_comment = forms.CharField(label ="Nome", max_length=100)
    email = forms.URLField(label="Email",max_length=200)
    comentario = forms.CharField(widget=forms.Textarea)

    def save(self, comment=None):
        name_comment = self.cleaned_data.get("name_comment")
        email = self.cleaned_data.get("email")
        comentario = self.cleaned_data.get("comentario")

        if comment:
            comment.name_comment = name_comment
            comment.email = email
            comment.comentario = comentario

        else:
            novo_comment = Comment(
                name_comment = name_comment,
                email = email,
                comentario = comentario

        )
        novo_comment.save()
        return novo_comment






