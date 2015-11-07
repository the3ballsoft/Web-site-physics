# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib import auth
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from .forms import LoginForm



class LoginRedirectView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("/docentes/home/")
        return redirect("/docentes/login/")

class LoginView(TemplateView):
    template_name = 'login.html'
    
    def get(self, request):
        ctx = { 'login_form' : LoginForm() }
        if request.user.is_authenticated():
            return redirect("/docentes/home/")

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = LoginForm(request.POST)     # create form object
        args = {}
        args.update(csrf(request))
        args['login_form'] = LoginForm()

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if user.es_docente:
                        auth.login(request, user)
                        return redirect("/docentes/home/")
                    else:
                        args['msg'] = 'El usuario no es un docente registrado'
                        return render(request, 'login.html', args)
            else:
                args['msg'] = 'Nombre de usuario ó contraseña  incorrecta'
                return render(request, 'login.html', args)

        return render(request, 'login.html', args)

