from django.db import models

# Create your models here.
class order(models.Model):
    name = models.CharField(default='',max_length=50)
    email = models.CharField(default='',max_length=50)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)