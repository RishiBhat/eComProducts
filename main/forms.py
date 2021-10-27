from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta: 
        model= Product
        import_id_fields = ('prtotal')
        exclude=[""]
        skip_unchanged = True