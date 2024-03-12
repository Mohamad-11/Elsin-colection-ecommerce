from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='نام محصول ')
    slug = models.SlugField(max_length=25, verbose_name='اسلاگ ', unique=True)
    description = models.TextField(verbose_name='توضیحات ')
    price = models.IntegerField(verbose_name='قیمت محصول ')
    available = models.BooleanField(default=True, verbose_name='موجودی محصول ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='')


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')


