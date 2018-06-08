from django.shortcuts import render
from django.views import generic
from entry.models import PurchaseDetail
from .models import Item
# Create your views here.

def home(request):
    c_wood = 0
    c_fabric = 0
    c_glass=0
    c_leather=0
    c_steel = 0
    c_plastic = 0
    for pd in PurchaseDetail.objects.all():
        if(pd.product_name=="WOOD"):
            c_wood=c_wood + pd.quantity
        elif(pd.product_name=="FABRIC"):
            c_fabric = c_fabric + pd.quantity
        elif(pd.product_name=="GLASS"):
            c_glass = c_glass + pd.quantity
        elif(pd.product_name=="LEATHER"):
            c_leather = c_leather + pd.quantity
        elif(pd.product_name=="STEEL"):
            c_steel = c_steel + pd.quantity
        else:
            c_plastic = c_plastic + pd.quantity
    print("wOOD = ",c_wood)
    print("FABRIC = ",c_fabric)
    print("STEEL = ",c_steel)
    print("LEATHER = ",c_leather)
    print("GLASS = ",c_glass)
    print("PLASTIC = ",c_plastic)

    return render(request, 'home.html')

class viewInventoryView(generic.ListView):
    model =Item

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
