from django.contrib import admin
from .models import Material
from django_summernote.admin import SummernoteModelAdmin

class AdminMateriale(SummernoteModelAdmin):
	list_display=('titulo','descripcion','arichivo','created',)

admin.site.register(Material,AdminMateriale)