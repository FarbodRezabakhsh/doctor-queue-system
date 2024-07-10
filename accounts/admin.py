from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User, Profile, Wallet


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "phone_number", "is_staff", "is_active", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_verified")
    searching_fileds = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Main", {"fields": ("email", "phone_number", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
        ("group permissions", {"fields": ("groups", "user_permissions")}),
        ("important date", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["name", "user", "age", "gender"]

    readonly_fields = ["user", ]

    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["user", "name", "age", "gender"]


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["user", "balance"]
    readonly_fields = ["user", ]

    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["user", "balance"]


