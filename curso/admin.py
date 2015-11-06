from django.contrib import admin
from .models import Curso
from materiales.models import Material


class AdminCurso(admin.ModelAdmin):
	pass
	

admin.site.register(Curso,AdminCurso)