from django.db import models
from sitio_web.models import TimeStampedModel
from profiles.models import User
from curso.models import Curso

	

class Material(TimeStampedModel):
	titulo = models.CharField(max_length=255)
	descripcion = models.TextField()
	arichivo = models.FileField(upload_to='materiales/')
	asignatura = models.ForeignKey(Curso)
	docente = models.ForeignKey(User)

	def __unicode__ (self):
		return self.titulo
