# Generated by Django 4.2.11 on 2024-10-20 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pottompatti', '0017_karrier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pottompatti.productcategory', verbose_name='kategória'),
        ),
    ]