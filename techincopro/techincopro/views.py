from django.shortcuts import render

from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name = "index.html"

class Documents(TemplateView):
    template_name = "documents.html"
