from django.conf.urls import patterns, include, url
from . import views
from . import auth_views

urlpatterns = patterns('',
    url(r'^docente/$', auth_views.LoginRedirectView.as_view(), name="login-redirect"), #login
    url(r'^docentes/login/$', auth_views.LoginView.as_view(), name="login-docentes"),
    url(r'^docentes/logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/docente/'} , name="logout"),
    url(r'^docentes/home/$', views.HomeView.as_view(), name="docentes-home"),
)
