
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url  
from django.conf.urls import include
# from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    
    # *******************  FLIPMART URLS ***********************************
    path('', include('flipmart.urls')),




    # *******************  ADMIN URLS ***********************************
    path('admin/', views.home),
    path('temp/', views.home2),
    
    path('login/', views.login),

    # home themes
    path('dashboard/', views.dashboard), 


    # Categories
    path('Sub_Categories/', views.sub_categories), 
    path('add_level_1_category/', views.add_level_1_category), 
    path('add_level_2_category/', views.add_level_2_category), 
    path('add_level_3_category/', views.add_level_3_category), 
    path('add_level_4_category/', views.add_level_4_category), 
    path('add_level_5_category/', views.add_level_5_category), 

    path('get_level_2_category/', views.get_level_2_category), 
    path('get_level_3_category/', views.get_level_3_category), 
    path('get_level_4_category/', views.get_level_4_category), 
    path('get_level_5_category/', views.get_level_5_category), 

    # SUBMIT CATEGORIES FORM
    path('load_categories/', views.load_categories),
    path('submit_categories/', views.submit_categories), 
    path('delete_category/', views.delete_category), 

    # Product Forms
    path('product_form/', views.product_form), 
    path('product_form_submit/', views.product_form_submit),
    path('edit_product_form_submit/', views.edit_product_form_submit), 
    path('get_category_id/', views.get_category_id),
    path('edit_product/', views.edit_product), 


    # =============== Product Reviews ==============
    path('product_reviews/', views.product_reviews),

    # =============== Favourite Products ==============
    path('favourite_product/', views.favourite_product),

    # =============== Customers Details management ==============
    path('customers_details/', views.customer_details),

        # =============== Order management ==============
    path('order_management/', views.order_management),


    # ============= Catalog Management =======================
    path('catalog_management/', views.catalog_management),
    path('add_new_stock/', views.add_new_stock),
    

    # Tables Links
    path('product_table/', views.product_table) , 
    path('update_product_price/', views.update_product_price) , 


    path('table2/', views.table2), 

    # Banners
    path('banners/', views.Banners), 
    path('add_image_banner/', views.add_image_banner), 
    path('set_banners/', views.set_banners), 

    # Color Combination
    path('color_combination/', views.color_combination), 
    path('change_theme/', views.change_theme), 

    # Page Editing
    path('page_editing/', views.page_editing)

] + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
