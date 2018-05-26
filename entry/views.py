from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PurchaseForm,PurchaseDetailForm
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Purchase
from django.views import View
# Create your views here.

class PurchaseCreateView(generic.edit.CreateView):
    """
    CreateView to create new purchase
    This is a class based view for creating new Purchase objects
    """
    model = Purchase
    form_class = PurchaseForm
    template_name = 'entry/purchase.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class PurchaseDetailView(generic.detail.DetailView):
    """
    DetailView that has PurchaseDetail form 
    and shows some minor details entered 
    previously in Purchase form

    """
    model = Purchase
    template_name='entry/product_details.html'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        purchase = get_object_or_404(Purchase, pk=pk)

        return purchase

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['purchase'] = self.get_object()
        context['product_form'] = PurchaseDetailForm
        return context

    def post(self, request, *args, **kwargs):
        form = PurchaseDetailForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('home'))