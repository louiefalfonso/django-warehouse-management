from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_lists, name='products'),
    path('add-product', views.add_product, name="add-product"),
    path('<int:sid>', views.product_details, name="product-details"),
    path('edit/<int:id>', views.edit_product, name="edit-product"),
    path('delete/<int:id>', views.delete_product, name="delete-product"),
]
