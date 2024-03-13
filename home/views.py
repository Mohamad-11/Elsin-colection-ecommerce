from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from . models import Product, Category, Image
from django.contrib.humanize.templatetags.humanize import intcomma


# Create your views here.

class HomeView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'home/index.html', {'products': products})