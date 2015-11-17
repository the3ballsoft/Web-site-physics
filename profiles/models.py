# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from sitio_web.models import TimeStampedModel


class User(AbstractUser):
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="telefono")
    cedula = models.CharField(max_length=255, blank=True, null=True, verbose_name="cedula")
    es_docente = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="docentes/",blank=True, null=True,verbose_name="docentes")

    class Meta:
    	verbose_name = "Perfil de Usuario"
    	verbose_name_plural = "Perfiles de Usuarios"


    def __unicode__(self):
        return self.get_full_name()


    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
	
