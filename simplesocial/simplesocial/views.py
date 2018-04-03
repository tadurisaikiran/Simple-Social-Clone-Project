from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class Testpage(TemplateView):
        template_name = 'test.html'

class Thankspage(TemplateView):
        template_name = 'thanks.html'
