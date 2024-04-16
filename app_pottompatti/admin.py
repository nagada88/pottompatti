from django.contrib import admin
from .models import *
from django.conf import settings

# Register your models here.
# class MainPictureInline(admin.StackedInline):
#     model = AllatMainImage
#     extra = 0

# class AllatAdmin(admin.ModelAdmin):
#     inlines = [MainPictureInline]
    
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Hirek)
admin.site.register(TerjBeHozzank)
