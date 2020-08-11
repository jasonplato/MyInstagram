from django.shortcuts import render
from django.views.generic import TemplateView


class HelloWorld(TemplateView):
    template_name = 'helloworld.html'

# Create your views here.
