# Generated by Django 4.2.11 on 2024-04-09 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pottompatti', '0005_remove_productcategory_category_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
    ]
