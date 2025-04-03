from django.contrib import admin
from .models import *
from django.conf import settings
from solo.admin import SingletonModelAdmin
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['product_category']
    list_display = ['name', 'product_category']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_filter = ['product_main_category']
    list_display = ['name', 'colored_category']

    def colored_category(self, obj):
        color = {
            'tortak': 'red',
            'sutemenyek': 'green',
        }.get(obj.product_main_category, 'gray')

        return format_html(
            '<span style="color: white; background-color: {}; padding: 2px 6px; border-radius: 5px;">{}</span>',
            color,
            obj.get_product_main_category_display()
        )

    colored_category.short_description = 'Főkategória'

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Kapcsolat, SingletonModelAdmin)

