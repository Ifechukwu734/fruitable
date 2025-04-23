from django.contrib import admin
from django.http import HttpRequest
from . import models
# Register your models here.


class Index_page_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not models.Index_page.objects.exists()
    

class First_slider_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not models.First_slider.objects.exists()
    

class Second_slider_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not models.Second_slider.objects.exists()


class Slider_display(admin.ModelAdmin):
    list_display = ['name', 'image']


class Sign_up_image_display(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not models.Sign_up_image.objects.exists()

admin.site.register(models.Index_page, Index_page_admin)
admin.site.register(models.First_slider, First_slider_admin)
admin.site.register(models.Second_slider, Second_slider_admin)
admin.site.register(models.Sign_up_image, Sign_up_image_display)
admin.site.register(models.Otp_token_generator)