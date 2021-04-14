from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role, Team


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('userEmail', 'is_staff', 'is_active',)
    list_filter = ('userEmail', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('userName', 'userSurname', 'userTel', 'userEmail', 'userRole', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('userName', 'userSurname', 'userTel', 'userEmail', 'userRole', 'password1', 'password2')}
        ),
    )
    search_fields = ('userEmail',)
    ordering = ('userEmail',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Team)