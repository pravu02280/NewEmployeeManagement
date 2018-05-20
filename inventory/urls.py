from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('addtoinventory/', views.AddToInventoryView.as_view(), name='addtoinventory'),
    path('viewinventory/',views.viewInventoryView.as_view(), name='viewinventory'),
]
