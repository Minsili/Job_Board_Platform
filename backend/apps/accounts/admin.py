from django.contrib import admin
from .models import CustomUser, Role  # Import your models

# Register your models here
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
