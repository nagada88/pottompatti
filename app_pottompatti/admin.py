from django.contrib import admin
from .models import *
from django.conf import settings

# Register your models here.
# class MainPictureInline(admin.StackedInline):
#     model = AllatMainImage
#     extra = 0

# class AllatAdmin(admin.ModelAdmin):
#     inlines = [MainPictureInline]

class InstanceCounterMixin1():
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
        
class RendezvenyAdmin(InstanceCounterMixin1, admin.ModelAdmin):
    model = Rendezveny

class KarrierAdmin(InstanceCounterMixin1, admin.ModelAdmin):
    model = Karrier

class KapcsolatAdmin(InstanceCounterMixin1, admin.ModelAdmin):
    model = Kapcsolat

class EskuvoAdmin(InstanceCounterMixin1, admin.ModelAdmin):
    model = Eskuvo

class TerjBeHozzankAdmin(InstanceCounterMixin1, admin.ModelAdmin):
    model = TerjBeHozzank

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Hirek)
admin.site.register(TerjBeHozzank, TerjBeHozzankAdmin)
admin.site.register(Kapcsolat, KapcsolatAdmin)
admin.site.register(EskuvoKerdezzFelelek)
admin.site.register(Eskuvo, EskuvoAdmin)
admin.site.register(Rendezveny, RendezvenyAdmin)
admin.site.register(RendezvenyKerdezzFelelek)
admin.site.register(Karrier, KarrierAdmin)

