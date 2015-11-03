from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View

from .models import Presentacion, Noticias

from .models import Docentes, Galeria

from .helpers import get_object_or_None

class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['data'] = Presentacion.objects.get(pk=1)
		context['noticias'] = Noticias.objects.all()[:6]
		print context
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
		print context
		return context 

class CursosView(TemplateView):
	template_name = 'cursos.html'

class EventosView(TemplateView):
	template_name = 'eventos.html'

	def get_context_data(self, **kwargs):
		context = super(NoticiasView, self).get_context_data(**kwargs)
		context['eventos'] = Eventos.objects.all()
		return context 

class LaboratoriosView(TemplateView):
	template_name = 'laboratorios.html'

class MaterialesView(TemplateView):
	template_name = 'materiales.html'

class ContactenosView(TemplateView):
	template_name = 'contactenos.html'

class GaleriaView(TemplateView):
	template_name = 'galeria.html'

	def get_context_data(self, **kwargs):
		context = super(GaleriaView, self).get_context_data(**kwargs)
		context['galerias'] = Galeria.objects.all()
		print context
		return context 



class BlogView(TemplateView):
	template_name = 'blog.html'

