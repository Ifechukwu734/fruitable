from django.db import models
from django.contrib.auth.models import User
import secrets

# Create your models here.


class Index_page(models.Model):
    site_name = models.CharField(max_length=30)
    site_header = models.CharField(max_length=90)
    header_background = models.ImageField(upload_to='image')
    feature_1 = models.CharField(max_length=50)
    feature_text_1 = models.CharField(max_length=50)
    feature_2 = models.CharField(max_length=50)
    feature_text_2 = models.CharField(max_length=50)
    feature_3 = models.CharField(max_length=50)
    feature_text_3 = models.CharField(max_length=50)
    feature_4 = models.CharField(max_length=50)
    feature_text_4 = models.CharField(max_length=50)
    shop_heading = models.CharField(max_length=50)
    second_feature_1 = models.CharField(max_length=30)
    second_feature_1_image = models.ImageField(upload_to='image')
    second_feature_1_text = models.CharField(max_length=40)
    second_feature_2 = models.CharField(max_length=30)
    second_feature_2_image = models.ImageField(upload_to='image')
    second_feature_2_text = models.CharField(max_length=40)
    second_feature_3 = models.CharField(max_length=30)
    second_feature_3_image = models.ImageField(upload_to='image')
    second_feature_3_text = models.CharField(max_length=40)
    section_shop_heading = models.CharField(max_length=30)
    banner_header = models.CharField(max_length=40)
    banner_header_completion = models.CharField(max_length=40)
    banner_text = models.CharField(max_length=50)
    banner_image = models.ImageField(upload_to='image')
    banner_price = models.CharField(max_length=10)
    banner_quantity = models.IntegerField()
    best_seller_title = models.CharField(max_length=50)
    best_seller_text = models.CharField(max_length=200)
    satisfied_customers = models.IntegerField()
    quality_of_service = models.IntegerField()
    quality_certificates = models.IntegerField()
    available_products = models.IntegerField()
    footer_text = models.CharField(max_length=30)
    copyright_text = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Index_page'
        verbose_name_plural = 'Index_page'


    def __str__(self):
        return self.site_name
    

class First_slider(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name = 'First_slider'
        verbose_name_plural = 'First_slider'

    def __str__(self):
        return self.name


class Second_slider(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name = 'Second_slider'
        verbose_name_plural = 'Second_slider'

    def __str__(self):
        return self.name


class Sign_up_image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sign_up_image'
        verbose_name_plural = 'sign_up_image'


class Otp_token_generator(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    otp = models.CharField(max_length=7, default=secrets.token_hex(3))
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.otp