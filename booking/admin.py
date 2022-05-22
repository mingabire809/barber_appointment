from django.contrib import admin
from .models import Booking
from .serializers import BookingSerializer


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_reference_number', 'member', 'name', 'email', 'phone', 'booking_date',
        'hair_cut', 'extra_services', 'location', 'base_price', 'extra_price', 'total_price',
        'pay_now', 'payment_method', 'booking_date', 'paid', 'is_processed')

    def extra_services(self, obj):
        return "\n".join([p.products for p in obj.product.all()])

    search_fields = ('booking_reference_number', 'booking_user', 'booking_user_email')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('-booking_date', 'paid')


#    def email(self, obj):
#        return obj.email.email

#    def phonenumber(self, obj):
#        return obj.phonenumber.email


admin.site.register(Booking, BookingAdmin)
