from django.shortcuts import render
from django.views import generic
# Create your views here.
class HelpView(generic.TemplateView):
    template_name = 'help/help.html'
