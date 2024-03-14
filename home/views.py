from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from . models import Product, Category, Image
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib import messages

# Create your views here.

class HomeView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            product.price = '{:,.0f}'.format(product.price)
        return render(request, 'home/index.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        products = get_object_or_404(Product, slug=slug)
        products.price = '{:,.0f}'.format(products.price)
        images = Image.objects.all()
        return render(request, 'home/product_detail.html', {'product': products, 'images': images})

