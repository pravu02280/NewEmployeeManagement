from django.shortcuts import render
from django.views import generic
from entry.models import PurchaseDetail
# Create your views here.

def home(request):
    c_wood = 0
    c_fabric = 0
    c_glass=0
    c_leather=0
    c_steel = 0
    for pd in PurchaseDetail.objects.all():
        if(pd.product_name=="WOOD"):
            c_wood=c_wood + pd.quantity
        if(pd.product_name=="FABRIC"):
            c_fabric = c_fabric + pd.quantity
        if(pd.product_name=="GLASS"):
            c_glass = c_glass + pd.quantity
        if(pd.product_name=="LEATHER"):
            c_leather = c_leather + pd.quantity
        if(pd.product_name=="STEEL"):
            c_steel = c_steel + pd.quantity
        
    print("wOOD = ",c_wood)
    print("FABRIC = ",c_fabric)
    print("STEEL = ",c_steel)
    print("LEATHER = ",c_leather)
    print("GLASS = ",c_glass)
    
    return render(request, 'home.html')

class viewInventoryView(generic.TemplateView):
    template_name = 'inventory/viewinventory.html'
