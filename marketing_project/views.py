from django.views.generic import TemplateView
from django.shortcuts import render



class Marketing(TemplateView):
    template_name = "index.html"


class Login(TemplateView):
    template_name = "home.html"