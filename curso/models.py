from django.db import models
from profiles.models import User

class Curso(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion =models.TextField()
	cover = models.ImageField(upload_to="cursos/",verbose_name="Imagen representativa")
	


	def __unicode__ (self):
		return self.nombre