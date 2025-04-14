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

@admin.register(TortaKepek)
class TortaKepekAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'photo_thumbnail')
    readonly_fields = ('photo_preview',)

    def photo_thumbnail(self, obj):
        if obj.photo_tumb:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', obj.photo_tumb.url)
        return "—"
    photo_thumbnail.short_description = 'Előnézet'

    def photo_preview(self, obj):
        if obj.photo_tumb:
            return format_html('<img src="{}" style="max-height: 300px;" />', obj.photo_tumb.url)
        return "Nincs előnézet"
    photo_preview.short_description = 'Jelenlegi kép'

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Kapcsolat, SingletonModelAdmin)

