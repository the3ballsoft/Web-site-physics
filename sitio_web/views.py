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