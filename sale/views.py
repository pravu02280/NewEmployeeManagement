from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SalesForm,SalesDetailForm
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Sale,SaleDetail
from django.views import View
from django.utils import timezone
# Create your views here.

class SalesCreateView(generic.edit.CreateView):
    """
    CreateView to create new purchase
    This is a class based view for creating new Purchase objects
    """
    model = Sale
    form_class = SalesForm
    template_name = 'sale/sales.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class SalesDetailView(generic.detail.DetailView):
    """
    DetailView that has SalesDetail form 
    and shows some minor details entered 
    previously in Purchase form

    """
    model = Sale
    template_name='sale/sales_detail.html'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        sales = get_object_or_404(Sale, pk=pk)

        return sales

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['sales'] = self.get_object()
        context['product_form'] = SalesDetailForm
        return context

    def post(self, request, *args, **kwargs):
        form = SalesDetailForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('home'))

class SalesListView(generic.list.ListView):
    model =Sale

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
