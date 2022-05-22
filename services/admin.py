from django.contrib import admin
from .models import HairCut, ExtraService


# Register your models here.

class HaircutAdmin(admin.ModelAdmin):
    list_display = ('hair_cut_type', 'price', 'picture')
    search_fields = ('HaircutType', 'price', 'picture')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ExtraServiceAdmin(admin.ModelAdmin):
    list_display = ('type_of_service', 'service_price', 'service_picture')
    search_fields = ('type_of_service', 'service_price')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(HairCut, HaircutAdmin)
admin.site.register(ExtraService, ExtraServiceAdmin)
