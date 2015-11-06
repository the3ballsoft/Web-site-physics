from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View



class LoginView(TemplateView):
	template_name = 'login.html'