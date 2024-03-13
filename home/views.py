from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from . models import Category, Product, Image

# Create your views here.


class HomeView(View):

    def get(self, request, ):
        products = Product.objects.get(available=True,)
        images = Image.objects.all()
        formatted_price = "{:.3f}".format(Product.price / 1000)
        # formatted_price.replace(',', '،')
        return render(request, 'home/index.html', {'products': products, 'images': images,
                                                   'formatted_price': formatted_price})
