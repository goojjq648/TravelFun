from django.contrib import admin
from .models import Member

class CustomUserAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('username', 'full_name', 'email', 'level', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('level', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'full_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email', 'level')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Important dates', {'fields': ('date_joined', 'last_updated')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'password1', 'password2', 'level'),
        }),
    )

admin.site.register(Member, CustomUserAdmin)
