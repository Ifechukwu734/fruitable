from django.contrib import admin
from . import models
# Register your models here.

class Product_display(admin.ModelAdmin):
    list_display = ['product_name', 'product_category', 'price', 'best_seller']


class Featured_product_display(admin.ModelAdmin):
    list_display = ['product_name', 'product_category', 'price']


class Comment_display(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment']
    

class Ordered_products_display(admin.ModelAdmin):
    list_display = ['product_name','order_id', 'product_price', 'product_quantity']
    readonly_fields = ('product_name','order_id', 'product_price', 'product_quantity')


class Billing_details_display(admin.ModelAdmin):
    list_display = ['first_name','order_id', 'local_pickup', 'total_items', 'total_order_price', 'paid']
    readonly_fields = ('first_name','order_id', 'local_pickup', 'total_items', 'total_order_price', 'paid')


admin.site.register(models.Products, Product_display)
admin.site.register(models.Product_category)
admin.site.register(models.Comment, Comment_display)
admin.site.register(models.Featured_products, Featured_product_display)
admin.site.register(models.Billing_details, Billing_details_display)
admin.site.register(models.Ordered_products, Ordered_products_display)