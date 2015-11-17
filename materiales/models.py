# -*- coding: utf-8 -*-
from django.db import models
from sitio_web.models import TimeStampedModel
from profiles.models import User
from curso.models import Curso


	

class Material(TimeStampedModel):
	titulo = models.CharField(max_length=255, blank=True, null=True)
	descripcion = models.TextField()
	arichivo = models.FileField(upload_to='materiales/', blank=True, null=True)
	curso =  models.ForeignKey(Curso)
	docente = models.ForeignKey(User)

	class Meta:
		verbose_name = 'Material Academico'
		verbose_name_plural = 'Materiales Academicos '

	def __unicode__ (self):
		return self.titulo
