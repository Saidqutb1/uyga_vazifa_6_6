from django.contrib import admin
from .models import CustomUser
# Register your models here.

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'firstname', 'date_joined')
#     list_filter = ['is_staff', 'is_superuser', 'first_name', 'last_name']
#
# admin.site.register(CustomUserAdmin, CustomUser)

admin.site.register(CustomUser)