from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_lists, name='product-lists'),
    path('add-product', views.add_product, name="add-product"),
]
