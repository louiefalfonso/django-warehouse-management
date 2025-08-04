from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

def product_lists(request):
    return render(request, "product/product_list.html",{"products": Product.objects.all()})




