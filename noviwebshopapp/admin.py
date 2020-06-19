from django.contrib import admin
from noviwebshopapp.models.painting import Painting
from noviwebshopapp.models.user_profile_info import UserProfileInfo
from noviwebshopapp.models.order import Order

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'available', 'rented_by', 'rented_till')
    list_filter = ('author', 'available', 'rented_by')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'author', 'image', 'price')
        }),
        ('Availability', {
            'fields': ('available', 'rented_by', 'rented_from', 'rented_till')
        })
    )

# Register your models here.
admin.site.register(Painting, PaintingAdmin)
admin.site.register(UserProfileInfo)
admin.site.register(Order)
