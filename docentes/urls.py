from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^docentes/login/$', views.LoginView.as_view(), name="login"), #login
)
