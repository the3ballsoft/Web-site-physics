from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name="index"), #search

    url(r'^docentes/$', views.TeachingView.as_view(), name="plantaDocente"), #search

    url(r'^noticias/$', views.NoticiasView.as_view(), name="noticias"), #search
    url(r'^cursos/$', views.CursosView.as_view(), name="cursos"), #search
    url(r'^eventos/$', views.EventoView.as_view(), name="evento"), #search
    url(r'^laboratorios/$', views.LaboratorioView.as_view(), name="laboratorios"), #search
    url(r'^materiales/$', views.MaterialesView.as_view(), name="materiales"), #search
    url(r'^contactenos/$', views.ContactenosView.as_view(), name="contactenos"), #search
    url(r'^galeria/$', views.GaleriaView.as_view(), name="galeria"), #search


)
