from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid
# Create your models here.


class Product_category(models.Model):
    name = models.CharField(max_length=50)
    number_of_post = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product_category'
        verbose_name_plural = 'Product_categories'


class Products(models.Model):
    QUALITY = (
        ('Organic', 'Organic'),
        ('Fresh', 'Fresh'),
        ('Sales', 'Sales'),
        ('Discount', 'Discount'),
        ('Expired', 'Expired')
    )

    product_name = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to='image', default=None)
    product_category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    price = models.IntegerField()
    short_description = models.TextField(max_length=300, )
    product_quality = models.CharField(choices=QUALITY, default=None)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    country_of_origin = models.CharField(max_length=30)
    product_health = models.CharField(max_length=20)
    weight = models.IntegerField()
    send_to_home_page = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', editable=False, max_length=30)
    best_seller = models.BooleanField(default=False)
    

    def get_absolute_url(self):
        kwargs = {
            'id': self.pk,
            'slug': self.slug
        }
        return reverse('product_detail', kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        value = self.product_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Comment(models.Model):
    post = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    comment_image = models.ImageField(upload_to='image', null=True)


class Featured_products(models.Model):
    QUALITY = (
        ('Organic', 'Organic'),
        ('Fresh', 'Fresh'),
        ('Sales', 'Sales'),
        ('Discount', 'Discount'),
        ('Expired', 'Expired')
    )
    product_name = models.CharField(max_length=30)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    product_image = models.ImageField(upload_to='image')
    product_category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    price = models.IntegerField()
    featured_price = models.IntegerField()
    short_description = models.TextField(max_length=300, )
    product_quality = models.CharField(choices=QUALITY)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    country_of_origin = models.CharField(max_length=30)
    product_health = models.CharField(max_length=20)
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', editable=False, max_length=30)
    display_on_sidebar = models.BooleanField(default=False)

    def get_absolute_url(self):
        kwargs = {
            'name': self.product_name,
            'pk': self.pk
        }
        return reverse('featured_details', kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        name = self.product_name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)


class Billing_details(models.Model):
    order_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    order_notes = models.TextField(max_length=500)
    local_pickup = models.BooleanField(default=False)
    total_order_price = models.FloatField(null=True)
    total_items = models.IntegerField(null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Billing_detail'
        verbose_name_plural = 'Billing_details'
    


class Ordered_products(models.Model):
    order_id = models.CharField(max_length=50)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to='images')
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
    total_order_price = models.FloatField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'Ordered_products'
        verbose_name_plural = 'Ordered_products'