from tkinter import Image

from django.db import models

# Create your models here.


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="زیر مجموعه ",
                                     related_name="subCategory", null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=30, verbose_name='نام دسته بندی ', unique=True)
    slug = models.SlugField(max_length=30)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی ')
    name = models.CharField(max_length=25, verbose_name='نام محصول ')
    slug = models.SlugField(max_length=25, verbose_name='اسلاگ ', unique=True)
    description = models.TextField(verbose_name='توضیحات ')
    price = models.IntegerField(verbose_name='قیمت محصول ')
    image = models.ImageField(upload_to='images/', verbose_name='عکس محصول ')
    available = models.BooleanField(default=True, verbose_name='موجودی محصول ')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name} - {self.created}'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')


