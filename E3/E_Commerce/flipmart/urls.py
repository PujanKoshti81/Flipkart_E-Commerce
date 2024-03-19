from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in),
    path('Login_check/', views.Login_check),
    path('logout_session/', views.logout_session),
    # =========  face login ============
    path('create_dataset/',views.Create_dataset),
    path('detect/',views.Detect),


    # =============== navigation pages ========================
    path('home/', views.flipmart_home),
    path('details/', views.details),
    path('category/', views.category),
    path('checkout/', views.checkout),
    path('my_wishlist/', views.my_wishlist),
    path('product_comparison/', views.product_comparison),
    path('shopping_cart/', views.shopping_cart),
    path('sign_in/', views.sign_in),
    path('track_orders/', views.track_orders),
    path('shop/', views.shop),

    # ============== cart =======================
    path('user_registration/', views.user_registration),
    path('add_to_cart/', views.add_to_cart),
    path('add_to_cart_details/', views.add_to_cart),
    path('delete_product_cart/', views.delete_product_cart),
    path('update_cart/', views.update_cart),

    # ============== review =========================
    path('submit_review/', views.review),

    # ============= wish_list =======================
    path('wish_list/', views.wish_list),

    # ============= compare =======================
    path('compare/', views.compare),
    path('del_pro_compare/', views.del_pro_compare),
    
    # ============= Place Order =======================
    path('place_order/', views.place_order),




]