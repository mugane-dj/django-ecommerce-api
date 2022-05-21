from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productID', 'product_name', 'product_description', 'product_price', 'product_image', 'category', 'status']
    list_display_links = ['productID', 'product_name', 'product_description', 'product_price', 'product_image', 'category', 'status']
    list_filter = ['productID', 'product_name', 'product_description', 'product_price', 'product_image', 'category', 'status']
    search_fields = ['productID', 'product_name', 'product_description', 'product_price', 'product_image', 'category', 'status']

admin.site.register(Product, ProductAdmin)
