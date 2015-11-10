from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View,UpdateView, DeleteView
from materiales.models import Material
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import CreateMaterial
from django.core.urlresolvers import reverse_lazy




class HomeView(TemplateView):
	template_name = 'index2.html'

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

       

class EventoView(TemplateView):
	template_name = 'veventos.html'

class EventoCrearView(TemplateView):
	template_name = 'ceventos.html'

class NoticiasView(TemplateView):
	template_name = 'vnoticias.html'

class NoticiasCrearView(TemplateView):
	template_name = 'cnoticias.html'