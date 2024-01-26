from django.urls import path

from .views import index, products, about, contact, product

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
]
