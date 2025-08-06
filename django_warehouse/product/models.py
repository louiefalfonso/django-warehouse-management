from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category_code = models.CharField(max_length=255)
    category_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category_code} - {self.category_name}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=255)
    product_number = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.product_name}"


