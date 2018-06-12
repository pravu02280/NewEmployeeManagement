from django import forms
from .models import Sale,SaleDetail
class SalesForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['invoice', 'ch_no', 'purchasers', 'date', 'description',]
class SalesDetailForm(forms.ModelForm):
    class Meta:
        model = SaleDetail
        fields = ['sales','product_name','quantity','rate','total','remarks',]