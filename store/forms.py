from django import forms
from .models import Product


class CategoryNameForm(forms.Form):
    new_name = forms.CharField(max_length=255)
    
class ProductForm(forms.Form):
    name = forms.CharField(max_length=255,required=False)
    small_description=forms.CharField(max_length=1500,required=False)
    description = forms.CharField(required=False)
    price = forms.DecimalField(max_digits=8, decimal_places=2,required=False)  
    promotion_price= forms.DecimalField(max_digits=8, decimal_places=2 ,required=False )
    quantity = forms.IntegerField(required=False,)


class NewProductForm(forms.Form):
    name = forms.CharField(max_length=255,required=True)
    small_description=forms.CharField(max_length=1500,required=True)
    description = forms.CharField(required=True)
    price = forms.DecimalField(max_digits=8, decimal_places=2,required=True)  
    promotion_price= forms.DecimalField(max_digits=8, decimal_places=2 ,required=False )
    # image = forms.ImageField(required=True)  
    quantity = forms.IntegerField(required=True,)





