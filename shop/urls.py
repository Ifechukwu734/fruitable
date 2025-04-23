from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_page, name='shop_page'),
    path('<str:name>-<int:product_id>', views.product_details, name='product_detail'),
    path('<str:name>-<int:product_id>/comment/', views.product_details, name='comment'),
    path('filter', views.filter_product, name="filter"),
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('featured_products/add_featured_product_to_cart', views.add_featured_product_to_cart, name='add_featured_product_to_cart'),
    path('delete_item', views.delete_item, name='delete_item'),
    path('cart/', views.cart_items, name='cart_items'),
    path('reload', views.reload, name='reload'),
    path('featured_products/', views.featured_products, name="featured_products"),
    path('filter_featured_products', views.filter_featured_product, name='filter_featured_products'),
    path('featured_products/<str:name>-<int:id>/', views.featured_details, name='featured_details'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('local_pickup', views.local_pickup, name='local_pickup')
   
]