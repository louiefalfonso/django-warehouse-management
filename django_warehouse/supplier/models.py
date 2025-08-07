from django.db import models

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    supplier_code = models.CharField(max_length=100, unique=True)
    supplier_company = models.CharField(max_length=255)
    supplier_email = models.EmailField(max_length=255, unique=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    contact_address = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.supplier_code} - {self.supplier_name}"
