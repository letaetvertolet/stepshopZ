from django.urls import path

from .views import index, products, about, contact, product

urlpatterns = [
    path('', index),
    path('products/', products),
    path('about/', about),
    path('contact/', contact),
    path('products/', product),
]
