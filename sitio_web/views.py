# -*- coding: utf-8 -*-
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Presentacion, Noticias

from .models import Docentes, Galeria, Evento, Ubicacion, Laboratorio, Frase
from materiales.models import Material
from .helpers import get_object_or_None
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings

class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['frase']  = Frase.objects.all().last()
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



def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
    return render(request, "contactenos.html", {'form': form})


class GaleriaView(TemplateView):
	template_name = 'galeria.html'

	def get_context_data(self, **kwargs):
		context = super(GaleriaView, self).get_context_data(**kwargs)
		context['galerias'] = Galeria.objects.all()
		
		return context 


