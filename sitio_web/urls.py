from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name="index"), #search
    url(r'^docentes/$', views.TeachingView.as_view(), name="plantaDocente"), #search
)
