# Generated by Django 5.0.1 on 2024-09-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_products_best_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('comment', models.TextField()),
            ],
        ),
    ]
