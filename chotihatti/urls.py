from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="chotihatti"),
    path('store', views.store, name="store"),
    path('single_product', views.single_product, name="single_product"),
    path('cart', views.cart, name="cart"),

]
