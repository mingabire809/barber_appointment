from django.contrib import admin
from .models import Premium


# Register your models here.

class PremiumAdmin(admin.ModelAdmin):
    list_display = ('premium_reference_number', 'member',
                    'name', 'email', 'phone', 'membership', 'price',
                    'date', 'expiry_date', 'balance', 'coupon', 'isExpired')
    search_fields = ('premium_reference_number', 'member',
                     'name', 'email', 'phone', 'membership', 'price',
                     'date', 'isExpired')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Premium, PremiumAdmin)
