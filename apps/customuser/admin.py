# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        ("User", {"fields": ("name", "phone_number")}),
    ) + auth_admin.UserAdmin.fieldsets
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_active",
        "is_superuser",
        "created",
        "modified",
    ]
    list_filter = ("is_admin", "is_active", "is_superuser", "groups")
    search_fields = ["username", "email", "first_name", "last_name", "phone_number"]
    ordering = ("-created",)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = ("id", "__str__", "natural_key", "codename", "content_type")
    list_filter = ("content_type",)
    search_fields = ("name",)

    def natural_key(self, obj):
        return obj.natural_key()


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    pass
