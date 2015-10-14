from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Presentacion
from .helpers import get_object_or_None

class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['data'] = Presentacion.objects.get(pk=1)
		
		return context


class NoticiasView(TemplateView):
	template_name = 'noticias.html'

class CursosView(TemplateView):
	template_name = 'cursos.html'

class EventosView(TemplateView):
	template_name = 'eventos.html'

class LaboratoriosView(TemplateView):
	template_name = 'laboratorios.html'

class MaterialesView(TemplateView):
	template_name = 'materiales.html'

class ContactenosView(TemplateView):
	template_name = 'contactenos.html'

class GaleriaView(TemplateView):
	template_name = 'galeria.html'

class BlogView(TemplateView):
	template_name = 'blog.html'