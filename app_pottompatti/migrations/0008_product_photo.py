# Generated by Django 4.2.11 on 2024-04-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_pottompatti", "0007_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                default="/app_pottompatti/img/bakery.jpg",
                upload_to="app_pottompatti/img/photos/",
                verbose_name="kép",
            ),
        ),
    ]