# Generated by Django 5.0.1 on 2024-09-21 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Product_category',
                'verbose_name_plural': 'Product_categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_id', models.UUIDField(null=True)),
                ('product_image', models.ImageField(default=None, upload_to='image')),
                ('price', models.IntegerField()),
                ('short_description', models.TextField(max_length=300)),
                ('product_quality', models.CharField(choices=[('Organic', 'Organic'), ('Fresh', 'Fresh'), ('Sales', 'Sales'), ('Discount', 'Discount'), ('Expired', 'Expired')], default=None)),
                ('description', models.TextField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('country_of_origin', models.CharField(max_length=30)),
                ('product_health', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
                ('send_to_home_page', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product_category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
