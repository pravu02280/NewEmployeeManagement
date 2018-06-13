from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PurchaseForm,PurchaseDetailForm
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Purchase,PurchaseDetail
from django.views import View
from django.utils import timezone
from inventory.models import Item

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
            data = request.POST.get('product_name')
            quantity = int(request.POST.get('quantity'))
            rate = int(request.POST.get('rate'))
            for item in Item.objects.all():
                if(data.lower() == item.item_name.lower()):
                    item.item_quantity = item.item_quantity + quantity
                    item.item_rate = rate
                item.save()
            form.save()
        return HttpResponseRedirect(reverse('home'))

class PurchaseListView(generic.list.ListView):
    model =Purchase

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context