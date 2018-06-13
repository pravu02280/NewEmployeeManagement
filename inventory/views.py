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
    #         wrate=pd.rate
    #     elif(pd.product_name=="FABRIC"):
    #         c_fabric = c_fabric + pd.quantity
    #         frate=pd.rate
    #     elif(pd.product_name=="GLASS"):
    #         c_glass = c_glass + pd.quantity
    #         grate=pd.rate
    #     elif(pd.product_name=="LEATHER"):
    #         c_leather = c_leather + pd.quantity
    #         lrate=pd.rate
    #     elif(pd.product_name=="STEEL"):
    #         c_steel = c_steel + pd.quantity
    #         srate=pd.rate
    #     else:
    #         c_plastic = c_plastic + pd.quantity
    #         prate=pd.rate
    # for item in Item.objects.all():
    #     if(item.item_name == 'Wood'):
    #         item.item_quantity = c_wood
    #         item.item_rate =wrate
    #     elif(item.item_name == 'Fabric'):
    #         item.item_quantity = c_fabric
    #         item.item_rate =frate
    #     elif(item.item_name == 'Leather'):
    #         item.item_quantity = c_leather
    #         item.item_rate =lrate
    #     elif(item.item_name == 'Glass'):
    #         item.item_quantity = c_glass
    #         item.item_rate =grate
    #     elif(item.item_name == 'Steel'):
    #         item.item_quantity = c_steel
    #         item.item_rate =srate
    #     else:
    #         item.item_quantity = c_plastic
    #         item.item_rate =prate
    #     item.save()

    return render(request, 'home.html')
class viewInventoryView(generic.ListView):
    model =Item

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
