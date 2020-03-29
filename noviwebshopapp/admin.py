from django.contrib import admin
from noviwebshopapp.models.painting import Painting
from noviwebshopapp.models.user_profile_info import UserProfileInfo

# Register your models here.
admin.site.register(Painting)
admin.site.register(UserProfileInfo)
