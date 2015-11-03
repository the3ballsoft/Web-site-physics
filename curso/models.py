from django.db import models
from profiles.models import User


class Curso(models.Model):
	nombre = models.CharField(max_length=255)
	
	
	def __unicode__ (self):
		return self.nombre