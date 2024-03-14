from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('detail/<slug:slug>', views.ProductDetailView.as_view(), name='detail_product'),

]