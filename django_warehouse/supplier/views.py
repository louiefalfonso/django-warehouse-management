from django.shortcuts import render, get_object_or_404, redirect

from .models import Supplier

# Display Supplier Lists
def supplier_lists(request):
    return render(request, "supplier/supplier-list.html", {"suppliers": Supplier.objects.all()})