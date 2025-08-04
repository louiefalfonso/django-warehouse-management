from django.forms import ModelForm, TextInput, IntegerField, Select, TextArea
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': TextInput(attrs={"type": "text"}),
            'product_brand': TextInput(attrs={"type": "text"}),
            'product_number': TextInput(attrs={"type": "text"}),
            'description': TextArea(attrs={"type": "text"}),
            'sku': TextInput(attrs={"type": "text"}),
            #'category': TextInput(attrs={"type": "text"}),
            'price': TextInput(attrs={"type": "number","min":"1.00", "max":"999.99"})
            'quantity': TextInput(attrs={"type": "number","min":"1", "max":"999"})
        }
        labels = {
            'product_name': 'Product Name',
            'product_brand': 'Product Brand',
            'product_number': 'Product Number',
            'description': 'Description',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity'
        }

