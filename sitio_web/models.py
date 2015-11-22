# -*- coding: utf-8 -*-
from django.db import models
from location_field.models.plain import PlainLocationField



class TimeStampedModel(models.Model):
    """
    Una clase abstracta que registra la fecha de creacion y
    modificacion del modelo
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    modified = models.DateTimeField(auto_now=True, verbose_name="fecha de actualizacion")

    class Meta:
        abstract = True

class Presentacion(models.Model):
	presentacion = models.TextField()
	mision = models.TextField()
	vision = models.TextField()
	objetivos = models.TextField()
	reglamentacion = models.TextField()

	class Meta:
		verbose_name = "Presentacion del Area"
		verbose_name_plural = "Presentacion del Area"

	def __unicode__(self):
		return 'Informacion basica'

class Noticias(TimeStampedModel):
	titulo = models.CharField(max_length=255, blank=True, null=True)
	informacion = models.TextField()
	imagen = models.ImageField(upload_to="noticias/",verbose_name="Noticias" , blank=True, null=True)

	class Meta:
		verbose_name = "Noticia"
		verbose_name_plural = "Noticias"
 
	def __unicode__(self):
		return self.titulo
	
class Laboratorio(TimeStampedModel):
	titulo = models.CharField(max_length=255, blank=True, null=True)
	informacion = models.TextField()
	imagen = models.ImageField(upload_to="laboratorios/",verbose_name="Laboratorios" , blank=True, null=True)
 
	def __unicode__(self):
		return self.titulo

class Imagen(TimeStampedModel):
	imagen = models.ImageField(upload_to="galeria/",verbose_name="Galeria")

	class Meta:
		verbose_name = "Imagen"
		verbose_name_plural = "Imagenes"

	def __unicode__(self):
		return self.imagen.name

class Galeria(TimeStampedModel):
	titulo = models.CharField(max_length=255, blank=True, null=True)
	imagenes =  models.ManyToManyField(Imagen)

	class Meta:
		verbose_name = "Galeria de Imagenes"
		verbose_name_plural = "Galerias de Imagenes"

	def __unicode__(self):
		return self.titulo


class Evento(models.Model):
	titulo = models.CharField(max_length=255, blank=True, null=True)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to="eventos/", verbose_name="Evento")
	fecha = models.DateField( blank=True)
	hora = models.TimeField( blank=True)
	

	class Meta:
		verbose_name = "Programar Evento"
		verbose_name_plural = "Programacion de Eventos"
	
	

	def __unicode__(self):
		return self.titulo
	


class Docentes(models.Model):
	imagen = models.ImageField(upload_to="docentes/",verbose_name="Galeria",blank=True, null=True)
	nombre = models.CharField(max_length=255, blank=True, null=True)
	correo = models.CharField(max_length=255, blank=True, null=True)
	telefono = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = "Planta Docente"
		verbose_name_plural = "Planta Docente"

	def __unicode__(self):
		return self.nombre

class Social(models.Model):
	nombre = models.CharField(max_length=255, blank=True, null=True)
	link = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = "Red Social"
		verbose_name_plural = "Redes Sociales"

	def __unicode__(self):
		return self.nombre


class Ubicacion(models.Model):
	ciudad = models.CharField(max_length=255)
	localizacion = PlainLocationField(based_fields=[ciudad], zoom=15)

	class Meta:
		verbose_name = "Ubicacion de la Universidad"
		verbose_name_plural = "Ubicacion de la Universidad"

	def __unicode__(self):
		return self.ciudad

class Frase(models.Model):
	frase = models.TextField()
	autor  = models.CharField(max_length=255, blank=True, null=True)

	def __unicode__(self):
		return self.frase

