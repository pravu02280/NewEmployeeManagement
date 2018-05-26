from django import forms
from .models import Purchase,ProductDetails
class purchaseform(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['invoice', 'ch_no', 'vendor', 'date', 'description',]
class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = ['product_name','quantity','rate','total','remarks',]