from django.contrib import admin
from . models import Product, Category, Image
from django.utils.html import format_html, mark_safe
from django.conf import settings


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'is_sub')
    list_filter = ('is_sub', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="%s%s" width="50px" height="50px" style="border-radius:10px;" />'.format(obj.image.url, obj))

    list_display = ('name', 'category', 'price', 'image_tag')
    raw_id_fields = ('category',)



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')
