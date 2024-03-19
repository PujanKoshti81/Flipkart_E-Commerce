
# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('details/', views.details),
    path('category/', views.category),
    path('checkout/', views.checkout),
    path('my_wishlist/', views.my_wishlist),
    path('product_comparison/', views.product_comparison),
    path('shopping_cart/', views.shopping_cart),
    path('sign_in/', views.sign_in),
    path('track_orders/', views.track_orders),





    path('user_registration/', views.user_registration),


]
