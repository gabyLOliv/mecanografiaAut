from django.contrib import admin
from django.contrib.auth import admin as auth
from .models import UUIDUser
# Register your models here.


# UserAdmin
# - - - - - - - - - - - - - - - - - - -
class UserAdmin(auth.UserAdmin):

    fieldsets = (
        ('Personal info', {'fields': ('username', 'password', 'email', 'matricula', 'tipo_user')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')


# Register
# - - - - - - - - - - - - - - - - - - -
admin.site.register(UUIDUser, UserAdmin)
# admin.site.register(UUIDUser)