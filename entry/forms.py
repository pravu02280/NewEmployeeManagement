from django import forms
from .models import Purchase,PurchaseDetail
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['invoice', 'ch_no', 'vendor', 'date', 'description',]
class PurchaseDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetail
        fields = ['purchase','product_name','quantity','rate','total','remarks',]