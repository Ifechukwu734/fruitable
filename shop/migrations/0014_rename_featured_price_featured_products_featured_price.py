# Generated by Django 5.0.1 on 2024-09-29 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_featured_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featured_products',
            old_name='Featured_price',
            new_name='featured_price',
        ),
    ]
