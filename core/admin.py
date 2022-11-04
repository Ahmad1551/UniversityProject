from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "is_active", "created_at", )
    list_filter = ("user_type", "is_active", "is_superuser", "is_staff", )
    ordering = ("is_active", "-id",)
    search_fields = ("username", "first_name", "last_name", "email",)

    fieldsets = (
        (None, {"fields": ("username", "password", )}, ),
        ("Personal info", {"fields": ("first_name", "last_name", "phone_number", "email", "user_type", )}, ),
        ("Association", {"fields": ("organization",)},),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",)},),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", ),
        }),
    )


admin.site.register(User, UserAdmin)
