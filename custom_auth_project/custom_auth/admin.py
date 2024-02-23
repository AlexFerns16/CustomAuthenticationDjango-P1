from django.contrib import admin
from custom_auth.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(CustomUser)
