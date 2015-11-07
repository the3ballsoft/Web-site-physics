from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View

class HomeView(TemplateView):
	template_name = 'home.html'