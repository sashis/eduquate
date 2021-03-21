from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Tutor


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = 'email', 'get_full_name', 'is_tutor', 'is_active'
    list_filter = 'is_tutor', 'is_active'
    readonly_fields = 'is_tutor',
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('права', {
            'fields': [('is_active', 'is_tutor')]
        }),
        ('личные данные', {
            'fields': (('first_name', 'last_name'), 'birthdate', 'gender', 'image', 'resume')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        ('права', {
            'classes': ('wide',),
            'fields': [('is_active', 'is_tutor')]
        }),
        ('личные данные', {
            'fields': (('first_name', 'last_name'), 'birthdate', 'gender', 'image', 'resume')
        }),
    )
    search_fields = ('email', 'last_name')
    ordering = ('last_name',)

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'имя/фамилия'
    get_full_name.admin_order_field = 'last_name'

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return []
        return super().get_readonly_fields(request, obj)


admin.site.unregister(Group)
