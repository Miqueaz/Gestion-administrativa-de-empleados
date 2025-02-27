from email import message
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from . import forms
from . import models
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'home/index.html'
    context = {}
    template = "index"
    
    def get(self, request):
        self.context = {
            "template": self.template
        }
        return render(request, self.template_name, self.context)
    
class LogIn(generic.TemplateView):
    template_name = 'home/LogIn.html'
    context = {}
    user = ""
    password = ""
       
    
    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/OPPENHEIMER/")
        else:
            messages.success(request, 'La contraseña o el usuario ingresados son incorrectos')
            return redirect("/inicio_sesion")
        
class LogOut(generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, 'has cerrado sesion')
        return redirect("/")
    
class about(generic.TemplateView):
    template_name = 'home/about.html'
    context = {}
    template = "about"
    
    def get(self, request):
        self.context = {
            'template': self.template
        }
        return render(request, self.template_name, self.context)
    

    

