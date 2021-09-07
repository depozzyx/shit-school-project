from django.contrib import admin
from .models import Category, Product, Order


class View:
    def __new__(cls, obj):
        class ViewAll(admin.ModelAdmin):
            list_display = obj.__dict__.get('__doc__').split('(')[1][:-1].split(', ')

        return obj, ViewAll


admin.site.register(*View(Category))
admin.site.register(*View(Product))
admin.site.register(*View(Order))
