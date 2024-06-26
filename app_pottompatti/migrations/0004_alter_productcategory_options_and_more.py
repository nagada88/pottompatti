# Generated by Django 4.2.11 on 2024-04-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pottompatti', '0003_allaslehetoseg_kapcsolat_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'kategória', 'verbose_name_plural': 'kategóriák'},
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='product_main_category',
            field=models.CharField(choices=[('Torták', 'Tortak'), ('Sütemények', 'Sutemenyek')], default='tortak', max_length=10, verbose_name='főkategória'),
        ),
        migrations.DeleteModel(
            name='ProductMainCategory',
        ),
    ]
