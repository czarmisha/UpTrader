from django.contrib import admin
from .models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url', 'named_url')
    list_filter = ('parent',)

    inlines = [
        MenuItemInline,
    ]

admin.site.register(MenuItem, MenuItemAdmin)
