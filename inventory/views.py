from django.shortcuts import render
from django.views import generic
# Create your views here.

def home(request):
    return render(request, 'home.html')

class AddToInventoryView(generic.TemplateView):
    template_name = 'inventory/addtoinventory.html'

class viewInventoryView(generic.TemplateView):
    template_name = 'inventory/viewinventory.html'
