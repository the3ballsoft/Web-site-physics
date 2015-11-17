from django.contrib import admin
from .models import Material
from curso.models import Curso
from django_summernote.admin import SummernoteModelAdmin

class AdminMateriale(admin.ModelAdmin):
	
	list_display=('titulo','descripcion','arichivo','created','docente','curso','tipo',)

	

admin.site.register(Material,AdminMateriale)