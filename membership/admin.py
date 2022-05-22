from django.contrib import admin
from .models import Membership


# Register your models here.
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'duration')
    search_fields = ('name', 'price', 'duration')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Membership, MembershipAdmin)
