from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View,UpdateView, DeleteView, CreateView
from materiales.models import Material
from sitio_web.models import Noticias,Evento
from profiles.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import CreateMaterial
from django.core.urlresolvers import reverse_lazy




class HomeView(TemplateView):
	template_name = 'index2.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['material'] = Material.objects.filter(docente = self.request.user).count()
		context['evento'] = Evento.objects.all().count()
		context['noticia'] = Noticias.objects.all().count()
		print context
		return context 

class MaterialView(TemplateView):
	template_name = 'vmaterial.html'

	def get_context_data(self, **kwargs):
		context = super(MaterialView, self).get_context_data(**kwargs)
		context['data'] = Material.objects.filter(docente = self.request.user).values()
		
		return context

class MaterialCrearView(View):
	
	def get(self, request):
		user = request.user
		if request.method == 'GET':
			form = CreateMaterial()
			return render(request, 'cmaterial.html',{'form': form})


	def post(self, request):
		
		if request.method == 'POST':

			form = CreateMaterial(request.POST, request.FILES)

			
			if form.is_valid():
				material = form.save(commit=False)
				material.docente = request.user
				material.save()
				return redirect("/docentes/material/")
			else :

				return redirect("/docentes/crearmaterial")

class MaterialUpdate(UpdateView):
	model = Material
	fields = ['titulo', 'descripcion', 'arichivo','curso']
	template_name = 'umaterial.html'
	template_name_suffix = '_update_form'
	success_url='/docentes/material/'

class MaterialDelete(DeleteView):
    model = Material
    success_url = '/docentes/material/'
    template_name = 'dmaterial.html'

class ProfilelUpdate(UpdateView):
	model = User
	fields = ['first_name', 'last_name', 'username','email','phone','avatar']
	template_name = 'uperfil.html'
	template_name_suffix = '_update_form'
	success_url='/docente/'

class EventoView(TemplateView):
	template_name = 'veventos.html'

	def get_context_data(self, **kwargs):
		context = super(EventoView, self).get_context_data(**kwargs)
		context['evento'] = Evento.objects.all()
		print context
		return context

class EventoDelete(DeleteView):
    model = Evento
    success_url = '/docentes/eventos/'
    template_name = 'devento.html'

class EventoUpdate(UpdateView):
	model = Evento
	fields = ['imagen', 'titulo', 'descripcion']
	template_name = 'ueventos.html'
	template_name_suffix = '_update_form'
	success_url='/docentes/eventos/'

class EventoCrearView(CreateView):
	template_name = 'ceventos.html'
	model = Evento
	fields = ['titulo','descripcion','imagen']
	success_url='/docentes/eventos/'

class NoticiasView(TemplateView):
	template_name = 'vnoticias.html'

	def get_context_data(self, **kwargs):
		context = super(NoticiasView, self).get_context_data(**kwargs)
		context['noticias'] = Noticias.objects.all()
		print context
		return context


class NoticiasCrearView(CreateView):
	template_name = 'cnoticias.html'
	model = Noticias
	fields = ['titulo','informacion','imagen']
	success_url='/docentes/noticias/'

class NoticiaDelete(DeleteView):
    model = Noticias
    success_url = '/docentes/noticias/'
    template_name = 'dnoticia.html'

class NoticiaUpdate(UpdateView):
	model = Noticias
	fields = ['titulo', 'informacion', 'imagen']
	template_name = 'unoticias.html'
	template_name_suffix = '_update_form'
	success_url='/docentes/noticias/'
