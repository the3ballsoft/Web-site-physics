from django.contrib import admin
from .models import Presentacion ,Noticias ,Proyectos ,Galeria ,laboratorios, Docentes, Social, Ubicacion
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
	list_display = ('titulo','created','modified',)

class ProyectosAdmin(SummernoteModelAdmin):
	list_display = ('titulo','created','modified',)

class GaleriaAdmin(SummernoteModelAdmin):

	list_display = ('titulo','created','modified','reimagen',)

	def reimagen(self, obj):

	    if obj.imagen:
	        return '<img src="%s" width="400px" height="200px">' % (obj.imagen.url)
	    else:
	        return '<img src="%s" width="400px" height="200px">' % ('http://placehold.it/60x60')
	reimagen.allow_tags = True
	reimagen.admin_order_field = 'imagen'
	reimagen.short_description = 'Imagen'

class laboratoriosAdmin(SummernoteModelAdmin):
	pass

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

admin.site.unregister(Attachment)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Presentacion, PresentacionAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Proyectos, ProyectosAdmin)
admin.site.register(laboratorios, laboratoriosAdmin)
admin.site.register(Docentes, DocentesAdmin)