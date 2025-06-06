# Generated by Django 5.0.1 on 2024-10-07 14:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_featured_products_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured_products',
            name='id',
        ),
        migrations.AlterField(
            model_name='featured_products',
            name='product_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
