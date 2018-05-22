from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('viewinventory/',views.viewInventoryView.as_view(), name='viewinventory'),
]
