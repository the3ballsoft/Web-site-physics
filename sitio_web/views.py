# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View

from .models import Presentacion, Noticias

from .models import Docentes, Galeria, Evento, Ubicacion, Laboratorio
from materiales.models import Material
from .helpers import get_object_or_None

class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['data'] = Presentacion.objects.get(pk=1)
		context['noticias'] = Noticias.objects.all()[:5]
		
		return context



class TeachingView(TemplateView):
	template_name = 'plantaDocente.html'

	def get_context_data(self, **kwargs):
		context = super(TeachingView, self).get_context_data(**kwargs)
		context['docentes'] = Docentes.objects.all()
		return context



class NoticiasView(TemplateView):
	template_name = 'noticias.html'

	def get_context_data(self, **kwargs):
		context = super(NoticiasView, self).get_context_data(**kwargs)
		context['noticias'] = Noticias.objects.all()
		
		return context 

class CursosView(TemplateView):
	template_name = 'cursos.html'

class EventoView(TemplateView):
	template_name = 'eventos.html'

	def get_context_data(self, **kwargs):
		context = super(EventoView, self).get_context_data(**kwargs)
		context['eventos'] = Evento.objects.all()
		return context 

class LaboratorioView(TemplateView):
	template_name = 'laboratorios.html'
	def get_context_data(self, **kwargs):
		context = super(LaboratorioView, self).get_context_data(**kwargs)
		context['laboratorios'] = Laboratorio.objects.all()
		return context

class MaterialesView(TemplateView):
	template_name = 'materiales.html'

	def get_context_data(self, **kwargs):
		context = super(MaterialesView, self).get_context_data(**kwargs)

		context['materiales'] = Material.objects.all()

		return context



class ContactenosView(TemplateView):
	template_name = 'contactenos.html'

	def get_context_data(self, **kwargs):
		context = super(ContactenosView, self).get_context_data(**kwargs)
		context['ubicacion'] = Ubicacion.objects.all()
		
		return context 

class GaleriaView(TemplateView):
	template_name = 'galeria.html'

	def get_context_data(self, **kwargs):
		context = super(GaleriaView, self).get_context_data(**kwargs)
		context['galerias'] = Galeria.objects.all()
		
		return context 


