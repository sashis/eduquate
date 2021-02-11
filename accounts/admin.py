from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Tutor


class TeacherProfileInline(admin.TabularInline):
    model = Tutor
    can_delete = False
    # verbose_name = 'профиль учителя'
    # fields = 'resume',
    # fieldsets = (
    #     ('профиль учителя', {
    #         'fields': ('resume',)
    #     }),
    # )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = 'email', 'get_full_name', 'is_tutor', 'is_active'
    list_filter = 'is_tutor', 'is_active'
    readonly_fields = 'is_tutor',
    inlines = [TeacherProfileInline]
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('права', {
            'fields': ('is_staff', 'is_tutor', 'is_active')
        }),
        ('личные данные', {
            'fields': ('first_name', 'last_name', 'gender', 'birthdate', 'image')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        ('права', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_tutor', 'is_active'),
        }),
        ('личные данные', {
            'fields': ('first_name', 'last_name', 'image', 'gender', 'birthdate')
        }),
    )
    search_fields = ('email', 'last_name')
    ordering = ('last_name',)

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'имя/фамилия'
    get_full_name.admin_order_field = 'user__last_name'

    def get_inline_instances(self, request, obj=None):
        if not obj or not obj.is_tutor:
            return []
        return super().get_inline_instances(request, obj)

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields if obj else []


admin.site.unregister(Group)
