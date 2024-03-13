from django.contrib import admin
from . models import Product, Category, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'is_sub')
    list_filter = ('is_sub', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    raw_id_fields = ('category',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')

