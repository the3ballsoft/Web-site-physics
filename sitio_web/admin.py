# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Presentacion ,Noticias ,Galeria , Docentes, Social, Ubicacion, Imagen, Evento, Laboratorio,Frase
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment




class PresentacionAdmin(SummernoteModelAdmin):
	list_display = ('represantacion','remision','revision','reobjectivos',)



	def represantacion(self, obj):
		return obj.presentacion

	represantacion.allow_tags = True
	represantacion.admin_order_field = 'Informacion general'
	represantacion.short_description = 'Informacion general'

	def remision(self, obj):
		return obj.mision

	remision.allow_tags = True
	remision.admin_order_field = 'Mision'
	remision.short_description = 'Mision'

	def revision(self, obj):
		return obj.vision

	revision.allow_tags = True
	revision.admin_order_field = 'Vision'
	revision.short_description = 'Vision'

	def reobjectivos(self, obj):
		return obj.objetivos

	reobjectivos.allow_tags = True
	reobjectivos.admin_order_field = 'Objetivos'
	reobjectivos.short_description = 'Objetivos'

class NoticiasAdmin(SummernoteModelAdmin):
	list_display = ('titulo','created','modified','imagens',)

	def imagens(self, obj):
		if obj.imagen:
			return '<img src="%s" width="400px" height="200px">' % (obj.imagen.url)
		else:
			return '<img src="%s" width="400px" height="200px">' % ('http://placehold.it/400x200')
	imagens.allow_tags = True
	imagens.admin_order_field = 'imagen'
	imagens.short_description = 'Imagen'

class EventoAdmin(SummernoteModelAdmin):
	list_display = ('titulo','imagens','fecha','hora',)

	def imagens(self, obj):
		if obj.imagen:
			return '<img src="%s" width="400px" height="200px">' % (obj.imagen.url)
		else:
			return '<img src="%s" width="400px" height="200px">' % ('http://placehold.it/400x200')
	imagens.allow_tags = True
	imagens.admin_order_field = 'imagen'
	imagens.short_description = 'Imagen'

class LaboratorioAdmin(SummernoteModelAdmin):
	list_display = ('titulo','imagens',)

	def imagens(self, obj):
		if obj.imagen:
			return '<img src="%s" width="400px" height="200px">' % (obj.imagen.url)
		else:
			return '<img src="%s" width="400px" height="200px">' % ('http://placehold.it/400x200')
	imagens.allow_tags = True
	imagens.admin_order_field = 'imagen'
	imagens.short_description = 'Imagen'




class GaleriaAdmin(SummernoteModelAdmin):
	model = Imagen
	filter_horizontal = ('imagenes',)
	list_display = ('titulo','created','modified',)





class DocentesAdmin(SummernoteModelAdmin):
	list_display = ('nombre','correo','telefono','retornaimagen',)

	def retornaimagen(self, obj):
		if obj.imagen:
			return '<img src="%s" width="80px" height="80px">' % (obj.imagen.url)
		else:
			return '<img src="%s" width="80px" height="80px">' % ('http://placehold.it/60x60')
	retornaimagen.allow_tags = True
	retornaimagen.admin_order_field = 'imagen de perfil'
	retornaimagen.short_description = 'Imagen de perfil'

class SocialAdmin(SummernoteModelAdmin):
	list_display = ('nombre', 'retornarred',)

	def retornarred(self ,  obj):
		print obj.link
		return '<a href="%s">  %s </a>' % (obj.link,obj.link)

	retornarred.allow_tags = True
	retornarred.admin_order_field = 'Link'
	retornarred.short_description = 'Link'

class UbicacionAdmin(SummernoteModelAdmin):
	list_display = ('ciudad','localizacion',)



class fraseAdmin(admin.ModelAdmin):

	list_display = ('frase','autor',)
	def frase(self, obj):
		return obj.frase
	frase.admin_order_field = 'Frase'
	frase.short_description = 'Frase'

	
admin.site.unregister(Attachment)
admin.site.register(Frase, fraseAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Presentacion, PresentacionAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Docentes, DocentesAdmin)
admin.site.register(Imagen)
admin.site.register(Evento, EventoAdmin)