from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

# Display Product Lists
def product_lists(request):
    return render(request, "product/product-list.html",{"products": Product.objects.all()})

# Add New Product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product/product-lists")
    else:
        form = ProductForm()
    return render(request, "product/add-product.html", {"form": form}) 

# Display Product Details
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product/product-detail.html", {"product": product})


# Edit Product
def edit_produt(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product/product-details", id)
    else:
        form = ProductForm(instance=product)
    return render(request, "product/edit-product.html", {"form": form})

# Delete Product
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("product/product-lists")
    else:
        return render(request, "product/delete-product.html", {"product": product})