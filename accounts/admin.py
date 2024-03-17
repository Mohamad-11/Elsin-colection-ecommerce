from django.contrib import admin
from . models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from . forms import UserChangeForm, UserCreationForm
from django.utils.html import format_html


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    def avatar_tag(self, obj):
        return format_html('<img src="%s%s" width="50px" height="50px" style="border-radius:10px;" />'.format(obj.avatar.url))

    avatar_tag.short_description = 'Image'

    list_display = ('email', 'phone_number', 'avatar_tag', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Main', {'fields': ('email', 'phone_number', 'full_name', 'avatar', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),

    )
    add_fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password1', 'password2')})
    )
    search_fields = ('email', 'full_name')
    ordering = ('full_name', )
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

