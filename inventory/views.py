from django.shortcuts import render
from django.views import generic
from entry.models import PurchaseDetail
from .models import Item
from inventory.models import Item
from .models import Item
# Create your views here.

def home(request):
    """
    This commented code below counts the items from scratch
    This is not what we need
    Will use this if we fail to make good update from

    """
    # c_wood = 0
    # c_fabric = 0
    # c_glass=0
    # c_leather=0
    # c_steel = 0
    # c_plastic = 0
    # for pd in PurchaseDetail.objects.all():
    #     if(pd.product_name=="WOOD"):
    #         c_wood=c_wood + pd.quantity
    #     elif(pd.product_name=="FABRIC"):
    #         c_fabric = c_fabric + pd.quantity
    #     elif(pd.product_name=="GLASS"):
    #         c_glass = c_glass + pd.quantity
    #     elif(pd.product_name=="LEATHER"):
    #         c_leather = c_leather + pd.quantity
    #     elif(pd.product_name=="STEEL"):
    #         c_steel = c_steel + pd.quantity
    #     else:
    #         c_plastic = c_plastic + pd.quantity
    # for item in Item.objects.all():
    #     if(item.item_name == 'Wood'):
    #         item.item_quantity = c_wood
    #     elif(item.item_name == 'Fabric'):
    #         item.item_quantity = c_fabric
    #     elif(item.item_name == 'Leather'):
    #         item.item_quantity = c_leather
    #     elif(item.item_name == 'Glass'):
    #         item.item_quantity = c_glass
    #     elif(item.item_name == 'Steel'):
    #         item.item_quantity = c_steel
    #     else:
    #         item.item_quantity = c_plastic
    #     item.save()

    return render(request, 'home.html')
class viewInventoryView(generic.ListView):
    model =Item

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
