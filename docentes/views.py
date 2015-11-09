from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View

class HomeView(TemplateView):
	template_name = 'index2.html'

class MaterialView(TemplateView):
	template_name = 'vmaterial.html'

class MaterialCrearView(TemplateView):
	template_name = 'cmaterial.html'

class EventoView(TemplateView):
	template_name = 'veventos.html'

class EventoCrearView(TemplateView):
	template_name = 'ceventos.html'

class NoticiasView(TemplateView):
	template_name = 'vnoticias.html'

class NoticiasCrearView(TemplateView):
	template_name = 'cnoticias.html'