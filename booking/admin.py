from django.contrib import admin
from .models import Booking
from .serializers import BookingSerializer


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_reference_number', 'member', 'name', 'email', 'phone', 'booking_date',
        'hair_cut', 'extra_services', 'base_price', 'extra_price')
    search_fields = ('booking_reference_number', 'booking_user', 'booking_user_email')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


#    def email(self, obj):
#        return obj.email.email

#    def phonenumber(self, obj):
#        return obj.phonenumber.email


admin.site.register(Booking, BookingAdmin)
