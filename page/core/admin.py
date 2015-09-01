# _*_ coding: utf-8 _*_
from django.contrib import admin
from .models import Event, Contact, Comment

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery
from .models import GalleryExtended

class GalleryExtendedInline(admin.StackedInline):
    model = GalleryExtended
    can_delete = False

class GalleryAdmin(GalleryAdminDefault):

    inlines = [GalleryExtendedInline, ]


class  QuestionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem', 'slug',)




class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numero_telefone',)
    search_fields = ('nome', 'email')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'text', 'email')




admin.site.register(Event, QuestionAdmin)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
