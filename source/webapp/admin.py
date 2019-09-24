from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'category', 'balance', 'price']
    list_filter = ['category']
    list_display_links = ['pk', 'name']
    search_fields = ['name', 'category', 'price']
    fields = ['name', 'description', 'category']


admin.site.register(Product, ProductAdmin)
