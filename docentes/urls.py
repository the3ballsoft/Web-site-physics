from django.conf.urls import patterns, include, url
from . import views
from . import auth_views

urlpatterns = patterns('',
    url(r'^docente/$', auth_views.LoginRedirectView.as_view(), name="login-redirect"), #login
    url(r'^docentes/login/$', auth_views.LoginView.as_view(), name="login-docentes"),
    url(r'^docentes/logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/docente/'} , name="logout"),
    url(r'^docentes/home/$', views.HomeView.as_view(), name="docentes-home"),
   
    url(r'^docentes/material/$', views.MaterialView.as_view(), name="docentes-material"),
    url(r'^docentes/crearmaterial/$', views.MaterialCrearView.as_view(), name="docentes-crearmaterial"),
    url(r'^docentes/actualizarmaterial/(?P<pk>[\w-]+)/$', views.MaterialUpdate.as_view(), name="docentes-actualizarmaterial"),
    url(r'^docentes/eliminarmaterial/(?P<pk>[\w-]+)/$', views.MaterialDelete.as_view(), name="docentes-eliminarmaterial"),
    
    url(r'^docentes/eventos/$', views.EventoView.as_view(), name="docentes-evento"),
    url(r'^docentes/creareventos/$', views.EventoCrearView.as_view(), name="docentes-evento"),
    url(r'^docentes/noticias/$', views.NoticiasView.as_view(), name="docentes-noticias"),
    url(r'^docentes/crearnoticias/$', views.NoticiasCrearView.as_view(), name="docentes-crearnoticias"),
)
