# Generated by Django 4.2.11 on 2024-04-17 14:04

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):
    dependencies = [
        ("app_pottompatti", "0010_alter_hirek_content_alter_terjbehozzank_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hirek",
            name="content",
            field=django_quill.fields.QuillField(
                max_length=500, verbose_name="Hír szövege"
            ),
        ),
        migrations.AlterField(
            model_name="terjbehozzank",
            name="content",
            field=django_quill.fields.QuillField(verbose_name="Bemutatkozó szöveg"),
        ),
    ]