from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta: Product
    fields=['id','prname','prtype', 'pr','prprice','prqty', 'prtotal']
