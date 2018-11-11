from django.contrib import admin
from .models import Menu,SubMenu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('category_name')


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'dish_name', 'price')

admin.site.register(Menu)
admin.site.register(SubMenu)
# Register your models here.
