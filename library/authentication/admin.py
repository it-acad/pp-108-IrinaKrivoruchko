from django.contrib import admin

from .models import CustomUser


class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'middle_name', 'created_at', 'is_superuser')
    list_filter = ['first_name', 'created_at', 'is_superuser']
    # fields = [('first_name', 'last_name', 'middle_name'), 'email', ('role', 'is_active')]
    fieldsets = (
        ("Static Information", {
            'fields': ('email', 'created_at'),
        }),
        ("Dynamic Information", {
            'fields': ('role', 'is_active'),
        }),
    )
    readonly_fields = ('email', 'created_at')

    # search_fields = ['email', 'first_name', 'last_name', 'middle_name']



admin.site.register(CustomUser, AuthenticationAdmin)

