from django.contrib import admin
from .models import Member


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'username', 'phone_number', 'profile_picture')
    search_fields = ('email', 'full_name', 'username', 'phone_number', 'profile_picture')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Member, MemberAdmin)
