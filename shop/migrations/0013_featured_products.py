# Generated by Django 5.0.1 on 2024-09-29 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_rename_image_comment_comment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_image', models.ImageField(upload_to='image')),
                ('price', models.IntegerField()),
                ('Featured_price', models.IntegerField()),
                ('short_description', models.TextField(max_length=300)),
                ('product_quality', models.CharField(choices=[('Organic', 'Organic'), ('Fresh', 'Fresh'), ('Sales', 'Sales'), ('Discount', 'Discount'), ('Expired', 'Expired')])),
                ('description', models.TextField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('country_of_origin', models.CharField(max_length=30)),
                ('product_health', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default='', editable=False, max_length=30)),
                ('display_on_sidebar', models.BooleanField(default=False)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product_category')),
            ],
        ),
    ]
