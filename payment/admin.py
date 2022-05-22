from django.contrib import admin
from .models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_number', 'transaction_date', 'member',
                    'name', 'email', 'phone', 'payment_method', 'booking_reference_number',
                    'total_price', 'premium_reference_number', 'balance', 'coupon', 'premium_expiration')
    search_fields = ('transaction_number', 'transaction_date', 'member',
                     'name', 'email', 'phone', 'payment_method', 'booking_reference_number',
                     'total_price', 'premium_reference_number')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('-transaction_date', )


admin.site.register(Payment, PaymentAdmin)
