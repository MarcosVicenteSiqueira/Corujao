# _*_ coding: utf-8 _*_
from django.contrib import admin
from .models import Event, Contact,   Foto

class  QuestionAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    prepopulated_fields = {'slug':('titulo',)}


class GaleriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nome',)}

class FotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'descricao',)
    prepopulated_fields = {'slug':('name',)}





class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numero_telefone',)
    search_fields = ('nome', 'email')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'text', 'email')




admin.site.register(Event, QuestionAdmin)
admin.site.register(Contact)
admin.site.register(Foto, FotoAdmin)
