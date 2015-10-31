from django.contrib import admin
from .models import Material
from curso.models import Curso
from django_summernote.admin import SummernoteModelAdmin

class AdminMateriale(SummernoteModelAdmin):
	model = Curso
	filter_horizontal = ('curso',)
	list_display=('titulo','descripcion','arichivo','created','docente','activities_display',)

	def activities_display(self, obj):
		result = '<ul>'
		for c in obj.curso.all():
			result += '<li>%s</li>'% c
			result += '</ul>'
		return result

	activities_display.allow_tags = True
	activities_display.short_description = 'Asignatura'

admin.site.register(Material,AdminMateriale)