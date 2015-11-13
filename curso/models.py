# -*- coding: utf-8 -*-
from django.db import models
from profiles.models import User



class Curso(models.Model):
	nombre = models.CharField(max_length=255)

	class Meta:
		verbose_name = 'Asignatura'
		verbose_name_plural = 'Asignaturas'
	
	def __unicode__ (self):
		return self.nombre