# Generated by Django 5.0.1 on 2024-09-21 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_second_slider_rename_slider_first_slider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='first_slider',
            options={'verbose_name': 'First_slider', 'verbose_name_plural': 'First_slider'},
        ),
        migrations.AlterModelOptions(
            name='index_page',
            options={'verbose_name': 'Index_page', 'verbose_name_plural': 'Index_page'},
        ),
        migrations.AlterModelOptions(
            name='second_slider',
            options={'verbose_name': 'Second_slider', 'verbose_name_plural': 'Second_slider'},
        ),
    ]
