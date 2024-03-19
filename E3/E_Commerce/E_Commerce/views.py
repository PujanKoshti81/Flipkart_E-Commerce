from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.conf import settings
from django.http import JsonResponse
from django.core import serializers


# ------ FOR DIFFERENT LEVEL OF CATEGORIES -------------------
from .models import Category_level_1
from .models import Category_level_2
from .models import Category_level_3
from .models import Category_level_4
from .models import Category_level_5

from .models import All_categories


# ------------- FOR BANNER IMAGES -------------------
from .models import Banners_image

# --------------- FOR THEME MANAGEMENT ---------------
from .models import Color_theme

# --------------- PRODUCT FORM REGISTRATION Tables -----------------
from .models import Basic_product_form
from .models import Special_price
from .models import Pro_qty_advanced_inventory
from .models import Contents
from .models import Main_Image_and_Videos
from .models import Set_of_Images_and_Videos
from .models import Search_Engine_Optimization
from .models import Schedule_design_update




# from .models import Variant_products

import json

# from .models import Variant_products

from flipmart.models import User_registration
from flipmart.models import Order_details
from flipmart.models import Wish_list
from flipmart.models import Review

# ---------- BASIC PAGE RENDERING  ----------------------

def home(request):
    return render(request, 'admin/home.html')


def home2(request):
    return render(request, 'admin/home2.html')    

def login(request):
    return render(request, 'admin/login.html')


def product_table(request):
    product_form1 = Basic_product_form.objects.all()
    special_price = Special_price.objects.all()
    adv_inventory = Pro_qty_advanced_inventory.objects.all()
    description = Contents.objects.all()
    main_img_video = Main_Image_and_Videos.objects.all()
    set_of_img = Set_of_Images_and_Videos.objects.all()
    seo = Search_Engine_Optimization.objects.all()
    schedule_design = Schedule_design_update.objects.all()

    data = {
        "product_form" : product_form1,
        "special_price" : special_price,
        "adv_inventory" : adv_inventory,
        "description" : description,
        "main_img_video" : main_img_video,
        "set_of_img" : set_of_img,
        "seo" : seo,
        "schedule_design" : schedule_design
    }
    return render(request, 'admin/product_table.html', data)

def table2(request):
    return render(request, 'admin/table2.html')

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def product_form(request):
    ALL = All_categories.objects.all()
    
    categories = {
        "all" : ALL
    }
    return render(request, 'admin/product_form.html',categories)



# ==================== Products Reviews ================
def product_reviews(request):
    reviews = Review.objects.all()
    all = {
        "Review" : review
    } 
    return render(request,'admin/product_reviews.html',all)



# ==================== Favourite Products ================
def favourite_product(request):
    favourites = Wish_list.objects.all()
    all = {
        "favourites" : favourites
    } 
    return render(request,'admin/favourite_products.html',all)




# ==================== Order Management of Customers ================
def order_management(request):
    # Customers = User_registration.objects.all()
    Order_details = Order_details.objects.all()
    # data = []

    # for user in Customers:

    all = {
        "sale_history" : Order_details
    } 
    return render(request,'admin/order_management.html',all)


# ==================== Customer Details handling ================
def customer_details(request):
    Customers = User_registration.objects.all()
    all = {
        "Customers" : Customers
    } 
    return render(request,'admin/customer_details.html',all)



# ==================  Catalog Management ======================

def catalog_management(request):
    products = Basic_product_form.objects.all()
    product = {
        "products" : products
    }
    return render(request, 'admin/catalog_manage.html',product)


def add_new_stock(request):
    if request.method == 'GET':
        product = Basic_product_form.objects.get(id = request.GET.get('product_id'))
        if request.GET.get('new_stock') != None:
            product.product_quantity = int(product.product_quantity) + int(request.GET.get('new_stock'))
        elif request.GET.get('edit_stock') != None:
            product.product_quantity = request.GET.get('edit_stock')
        product.save()
        data = {
            "stock" : product.product_quantity,
            "id" : product.id
        }
        return JsonResponse(data)




def sub_categories(request):
    CL1 = Category_level_1.objects.all()
    ALL = All_categories.objects.all()
    data = {
        "all" : ALL,
        "category_level_1" : CL1,
    }
    return render(request, 'admin/category.html',data)


def Banners(request):
    banners = Banners_image.objects.all()
    b = {
        "banners" : banners
    }
    return render(request, 'admin/Banners.html',b)		

def color_combination(request):
    return render(request, 'admin/color_combination.html')

def page_editing(request):
    return render(request, 'admin/page_editing.html')	
# ---------------------------------------------------------

def load_categories(request):
    ALL = list(All_categories.objects.all().values())

    d = {
        "all" : ALL
    }
    return JsonResponse(d)




# ===========DELETE AND EDIT CATEGORIES ======================================
def delete_category(request):
    if request.method == "GET":
        CL = All_categories.objects.get(id = request.GET.get('id'))      
        # cl1 = Category_level_1.objects.get(category_name = CL.category_level_1)
        # cl1.delete()
        CL.delete()

        print(CL.category_level_1)
        ac = list(All_categories.objects.all().values())
        response = {
            "all" : ac
        }
        return JsonResponse(response)



# ============ IT WILL STORE CATEGORIES IN DATABASE==================
def submit_categories(request):	

    if request.method == "GET":
        All = All_categories()



        print(request.GET.get("category_level_1"))
        print(request.GET.get("category_level_1"))
        if request.GET.get("category_level_2") == "0":
            CL1 = Category_level_1.objects.get(id = request.GET.get("category_level_1"))
            All.category_level_1 = CL1.category_name
            All.category_level_2 = "0"	
            All.category_level_3 = "0"
            All.category_level_4 = "0"
            All.category_level_5 = "0"
            All.save()
            store = list(All_categories.objects.all().values())

            data = {
                "All" : store
            }

            return JsonResponse(data)
        

        if request.GET.get("category_level_3") == "0":
            CL1 = Category_level_1.objects.get(id = request.GET.get("category_level_1"))
            All.category_level_1 = CL1.category_name
            CL2 = Category_level_2.objects.get(id = request.GET.get("category_level_2"))
            All.category_level_2 = CL2.category_L2_name
            All.category_level_3 = "0"
            All.category_level_4 = "0"
            All.category_level_5 = "0"
            All.save()
            store = list(All_categories.objects.all().values())

            data = {
                "All" : store
            }

            return JsonResponse(data)
        

        if request.GET.get("category_level_4") == "0":
            CL1 = Category_level_1.objects.get(id = request.GET.get("category_level_1"))
            All.category_level_1 = CL1.category_name
            CL2 = Category_level_2.objects.get(id = request.GET.get("category_level_2"))
            All.category_level_2 = CL2.category_L2_name
            CL3 = Category_level_3.objects.get(id = request.GET.get("category_level_3"))
            All.category_level_3 = CL3.category_L3_name
            All.category_level_4 = "0"
            All.category_level_5 = "0"            
            All.save()
            store = list(All_categories.objects.all().values())

            data = {
                "All" : store
            }

            return JsonResponse(data)
        

        if request.GET.get("category_level_5") == "0":
            CL1 = Category_level_1.objects.get(id = request.GET.get("category_level_1"))
            All.category_level_1 = CL1.category_name
            CL2 = Category_level_2.objects.get(id = request.GET.get("category_level_2"))
            All.category_level_2 = CL2.category_L2_name
            CL3 = Category_level_3.objects.get(id = request.GET.get("category_level_3"))
            All.category_level_3 = CL3.category_L3_name
            CL4 = Category_level_4.objects.get(id = request.GET.get("category_level_4"))
            All.category_level_4 = CL4.category_L4_name
            All.category_level_5 = "0"            
            All.save()
            store = list(All_categories.objects.all().values())

            data = {
                "All" : store
            }

            return JsonResponse(data)
        
        
        else :
            CL1 = Category_level_1.objects.get(id = request.GET.get("category_level_1"))
            All.category_level_1 = CL1.category_name
            CL2 = Category_level_2.objects.get(id = request.GET.get("category_level_2"))
            All.category_level_2 = CL2.category_L2_name
            CL3 = Category_level_3.objects.get(id = request.GET.get("category_level_3"))
            All.category_level_3 = CL3.category_L3_name
            CL4 = Category_level_4.objects.get(id = request.GET.get("category_level_4"))
            All.category_level_4 = CL4.category_L4_name
            CL5 = Category_level_5.objects.get(id = request.GET.get("category_level_5"))
            All.category_level_5 = CL5.category_L5_name
            All.save()    
        

            store = list(All_categories.objects.all().values())

            data = {
                "All" : store
            }

            return JsonResponse(data)




# ============== THESE ARE ADD NEW LEVEL OF SUB-CATEGORIES ==========================

def add_level_1_category(request):
    if request.method == 'GET':
        obj = Category_level_1()
        obj.category_name = request.GET.get('category_1')
        obj.save()
        
        a = request.GET.get('category_1')
        o = Category_level_1.objects.get(category_name=a)
        idd = o.id
        new = serializers.serialize("json", [o])

        data_name = {
            "new":new
        }
        data_id ={
            "id" : idd
        }
        data = {
            "data_name" : data_name,
            "data_id" : data_id
        }
        return JsonResponse(data)

def get_level_2_category(request):
    if request.method == 'GET':
        CL1_iddd = request.GET.get('id')		
        store_CL2 = list(Category_level_2.objects.all().filter(CL1_id = CL1_iddd).values())
        
        data = {
            "store_CL2" : store_CL2
        }
        return JsonResponse(data)

def add_level_2_category(request):
    if request.method == "GET":
        CL2 = Category_level_2()
        CL2.category_L2_name = request.GET.get('category_2')
        
        idd = request.GET.get('ID_of_CL1')
        obj = Category_level_1.objects.get(id = idd)
        CL2.CL1_id = obj
        CL2.save()

        a = request.GET.get('category_2')
        o = Category_level_2.objects.get(category_L2_name=a)
        idd = o.id
        new = serializers.serialize("json", [o])

        data_name = {
            "new":new
        }
        data_id ={
            "id" : idd
        }
        data = {
            "data_name" : data_name,
            "data_id" : data_id
        }

        return JsonResponse(data)

def get_level_3_category(request):
    if request.method == 'GET':
        CL2_iddd = request.GET.get('id')		
        store_CL3 = list(Category_level_3.objects.all().filter(CL2_id = CL2_iddd).values())
        
        data = {
            "store_CL3" : store_CL3
        }
        return JsonResponse(data)		

def add_level_3_category(request):
    if request.method == "GET":
        CL3 = Category_level_3()
        CL3.category_L3_name = request.GET.get('category_3')
        
        idd = request.GET.get('ID_of_CL2')
        obj = Category_level_2.objects.get(id = idd)
        CL3.CL2_id = obj
        CL3.save()

        a = request.GET.get('category_3')
        o = Category_level_3.objects.get(category_L3_name=a)
        idd = o.id
        new = serializers.serialize("json", [o])

        data_name = {
            "new":new
        }
        data_id ={
            "id" : idd
        }
        data = {
            "data_name" : data_name,
            "data_id" : data_id
        }

        return JsonResponse(data)		


def get_level_4_category(request):
    if request.method == 'GET':
        CL3_iddd = request.GET.get('id')		
        store_CL4 = list(Category_level_4.objects.all().filter(CL3_id = CL3_iddd).values())
        
        data = {
            "store_CL4" : store_CL4
        }
        return JsonResponse(data)		

def add_level_4_category(request):
    if request.method == "GET":
        CL4 = Category_level_4()
        CL4.category_L4_name = request.GET.get('category_4')
        
        idd = request.GET.get('ID_of_CL3')
        obj = Category_level_3.objects.get(id = idd)
        CL4.CL3_id = obj
        CL4.save()

        a = request.GET.get('category_4')
        o = Category_level_4.objects.get(category_L4_name=a)
        idd = o.id
        new = serializers.serialize("json", [o])

        data_name = {
            "new":new
        }
        data_id ={
            "id" : idd
        }
        data = {
            "data_name" : data_name,
            "data_id" : data_id
        }

        return JsonResponse(data)	

def get_level_5_category(request):
    if request.method == 'GET':
        CL4_iddd = request.GET.get('id')		
        store_CL5 = list(Category_level_5.objects.all().filter(CL4_id = CL4_iddd).values())
        
        data = {
            "store_CL5" : store_CL5
        }
        return JsonResponse(data)		

def add_level_5_category(request):
    if request.method == "GET":
        CL5 = Category_level_5()
        CL5.category_L5_name = request.GET.get('category_5')
        
        idd = request.GET.get('ID_of_CL4')
        obj = Category_level_4.objects.get(id = idd)
        CL5.CL4_id = obj
        CL5.save()

        a = request.GET.get('category_5')
        o = Category_level_5.objects.get(category_L5_name=a)
        idd = o.id
        new = serializers.serialize("json", [o])

        data_name = {
            "new":new
        }
        data_id ={
            "id" : idd
        }
        data = {
            "data_name" : data_name,
            "data_id" : data_id
        }

        return JsonResponse(data)	

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++            


# ================ COLOR COMBINATION THEME ========================
def change_theme(request):
    if request.method == 'POST':
        clean11 = Color_theme.objects.all()
        clean11.delete()
        clr = Color_theme()
        clr.header = request.POST.get('head1')
        clr.sidebar = request.POST.get('side1')
        clr.background_color = request.POST.get('back111')
        clr.save()
        a = {
            "result" : True
        }
        return JsonResponse(a)

# =================== SAVE BANNER TO DB =========================
def add_image_banner(request):
    if request.method == 'POST' and request.FILES['banner']:
        B_img = Banners_image()
        a = request.FILES['banner']
        abc = request.FILES['banner']
        fs = FileSystemStorage()
        file_name = fs.save(abc.name,abc)
        uploaded_file_url = fs.url(file_name)

        B_img.image = uploaded_file_url
        B_img.save()

        return redirect('/banners/')


def set_banners(request):
    if request.method == "POST":
        ss = request.POST.getlist('set[]')
        default = Banners_image.objects.all()
        for i in default:
            i.status = False
            i.save()
        for i in ss:
            o = Banners_image.objects.get(id = i)
            o.status = True
            o.save()
        return redirect('/banners/')


def get_category_id(request):
    if request.method == 'POST':
        Obj = All_categories.objects.get(id = request.POST.get('id'))
        O = serializers.serialize("json",[Obj])
        data = {
            "obj" : O
        }
        return JsonResponse(data)



# =================== PRODUCTT FORM REGISTRATION ===================		

def product_form_submit(request):
    if request.method == 'POST' :	

        # ------ Special Price -----------------------------
        sp_price = Special_price()
        sp_price.special_price_from = request.POST.get('sp_price_min_date')
        sp_price.special_price_to = request.POST.get('sp_price_max_date')
        sp_price.special_price = request.POST.get('sp_product_price')
        sp_price.special_cost = request.POST.get('sp_product_cost')
        sp_price.mfr_suggested_retailer_price = request.POST.get('sp_retailer_price')
        sp_price.disp_actual_price = request.POST.get('display_actual_price')


        sp_price.actual_per_gm = request.POST.get('actual_per_gm')
        sp_price.sale_per_gm = request.POST.get('sale_per_gm')
        sp_price.actual_total_pcs_price = request.POST.get('actual_total_pcs_price')
        sp_price.sale_total_pcs_price = request.POST.get('sale_total_pcs_price')
        sp_price.actual_pckg_cost = request.POST.get('actual_pckg_cost')
        sp_price.sale_pckg_cost = request.POST.get('sale_pckg_cost')
        sp_price.actual_parcel_cost = request.POST.get('actual_parcel_cost')
        sp_price.sale_parcel_cost = request.POST.get('sale_parcel_cost')
        sp_price.actual_other_cost = request.POST.get('actual_other_cost')
        sp_price.sale_other_cost = request.POST.get('sale_other_cost')
        sp_price.actual_total_price = request.POST.get('actual_total_price')
        sp_price.sale_total_price = request.POST.get('sale_total_price')
        sp_price.strike_price = request.POST.get('strike_price')
        sp_price.strike_start = request.POST.get('strike_start')
        sp_price.strike_end = request.POST.get('strike_end')


        sp_price.save()



        # ------ Product Quantity Advanced Inventory -----------------------------
        adv_inventory = Pro_qty_advanced_inventory()
        if request.POST.get('manage_stock') == 'on':
            adv_inventory.manage_stock = True
        if request.POST.get('out_of_stock') != None: 
            adv_inventory.out_of_stock_threshold = request.POST.get('out_of_stock')
        if request.POST.get('min_qty_cart') != None:
            adv_inventory.min_qty_allowed_in_cart = request.POST.get('min_qty_cart')
        if request.POST.get('max_qty_cart') != None:
            adv_inventory.max_qty_allowed_in_cart = request.POST.get('max_qty_cart')
        if request.POST.get('qty_decimels') == 'on':
            adv_inventory.qty_uses_decimal = True
        if request.POST.get('multi_box_ship_btn') == 'on':
            adv_inventory.allow_multi_box_of_shipping = True
        if request.POST.get('back_orders') != None:
            adv_inventory.back_orders = request.POST.get('back_orders')
        if request.POST.get('Notify_for_Quantity_Below') != None:
            adv_inventory.notify_for_qty_below = request.POST.get('Notify_for_Quantity_Below')
        if request.POST.get('enable_qty_increment') == 'on':
            adv_inventory.enable_qty_increments = True
        if request.POST.get('stock_in') == 'on':
            adv_inventory.stock_status = True
        adv_inventory.save()

        # ---------- Detailed Description of product --------------
        desc = Contents()
        desc.full_description = request.POST.get('product_all_details')
        desc.main_description = request.POST.get('product_main_details')
        desc.save()

        # ---------- Images and Videos Uploading ------------------
        fs = FileSystemStorage()
        imgg = Main_Image_and_Videos()
        
        try:
            thumbnail = request.FILES['thumbnail_of_product']
            thumbnail_name = fs.save(thumbnail.name, thumbnail)
            upload_thumbnail_url = fs.url(thumbnail_name)
            imgg.thumbnail = upload_thumbnail_url
        except MultiValueDictKeyError:
            pass

        try:
            main_img = request.FILES['Main_image_of_product']
            main_img_name = fs.save(main_img.name, main_img)
            upload_main_img_url = fs.url(main_img_name)
            imgg.main_image = upload_main_img_url
            imgg.save()				

        except MultiValueDictKeyError:
            pass

        try:
            video = request.FILES['video_of_product']
            video_name = fs.save(video.name, video)
            upload_video_url = fs.url(video_name)
            imgg.url_of_videos = upload_video_url
        except MultiValueDictKeyError:
            pass

        try:
            images = request.FILES.getlist('images_of_product')
            for i in images:	
                img_set = Set_of_Images_and_Videos()
                img_set.main_img_id = imgg	
                images_name = fs.save(i.name, i)
                upload_images_url = fs.url(images_name)	
                img_set.url_of_images = upload_images_url
                img_set.save()	

        except MultiValueDictKeyError:
            pass

        # ---- File Upload method 1 ---------------
        # if request.method == 'POST' and request.FILES['imgg']:
        # abc = request.FILES['imgg']
        # fs = FileSystemStorage()
        # file_name = fs.save(abc.name,abc)
        # uploaded_file_url = fs.url(file_name)
        # print(uploaded_file_url)
        # print(abc.size)
        # product.image = uploaded_file_url
        # -----------------------------


        # ----------- Search Engine Optimization ---------------
        seo = Search_Engine_Optimization()
        seo.url_key = request.POST.get('url_key_seo')
        seo.meta_title = request.POST.get('meta_title_seo')
        seo.meta_keywords = request.POST.get('meta_keywords_seo')
        seo.meta_description = request.POST.get('meta_description_seo')
        seo.save()


        # ------------ Schedule Design Update ---------------------
        schedule = Schedule_design_update()
        schedule.schedule_design_start = request.POST.get('schedule_update_start')
        schedule.schedule_design_end = request.POST.get('schedule_update_end')
        schedule.new_layout = request.POST.get('new_layout')
        schedule.new_theme = request.POST.get('new_theme')
        schedule.save()


        # ---- object of Basic fields of product---------
        product = Basic_product_form()
        product.special_price_id = Special_price.objects.get(id = sp_price.id)
        product.adv_inventory_id = Pro_qty_advanced_inventory.objects.get(id = adv_inventory.id)
        product.contents_id = Contents.objects.get(id = desc.id)
        product.main_image_id = Main_Image_and_Videos.objects.get(id = imgg.id)
        product.seo_id = Search_Engine_Optimization.objects.get(id = seo.id)
        product.schedule_design_id = Schedule_design_update.objects.get(id = schedule.id)
        product.special_price_id = Special_price.objects.get(id = sp_price.id)
        
        product.product_name = request.POST.get('product_name')
        product.product_price = request.POST.get('product_price')
        product.tax_class = request.POST.get('tax_class')
        product.product_quantity = request.POST.get('product_quantity')
        product.length = request.POST.get('length_of_product')
        product.width = request.POST.get('width_of_product')
        product.height = request.POST.get('height_of_product')
        
        if request.POST.get('weight_of_product') != None:
            product.weight = request.POST.get('weight_of_product')

        Obj = All_categories.objects.get(id = request.POST.get('id_of_category'))

        product.category = Obj
        product.visibility = request.POST.get('visibility')
        product.set_pro_new_from = request.POST.get('new_pro_min_date')
        product.set_pro_new_to = request.POST.get('new_pro_max_date')
        if request.POST.get('featured') == 'on':
            product.featured = True
        if request.POST.get('gift_option') == 'on':
            product.gift = True




        product.save()

        return redirect("/product_form/")



# ======== PRODUCT EDIT ===================

def edit_product(request):
    if request.method == 'GET':
        product = Basic_product_form.objects.get(id = request.GET.get('id'))
        ALL = All_categories.objects.all()
    
        new = {
            "product" : product,
            "all" : ALL
        }
        return render(request,'admin/edit_product.html',new)




def edit_product_form_submit(request):
    if request.method == 'POST':        

        product = Basic_product_form()

        product_id = request.POST.get('product_id')
        category_idd = request.POST.get('id_of_category')
        special_price_idd = request.POST.get('special_price_id')
        adv_inventory_idd = request.POST.get('adv_inventory_id')
        contents_idd = request.POST.get('contents_id')
        seo_idd = request.POST.get('seo_id')
        schedule_design_idd = request.POST.get('schedule_design_id')

        # ------ Special Price -----------------------------
        sp_price = Special_price()
        sp_price.special_price_from = request.POST.get('sp_price_min_date')
        sp_price.special_price_to = request.POST.get('sp_price_max_date')
        sp_price.special_price = request.POST.get('sp_product_price')
        sp_price.special_cost = request.POST.get('sp_product_cost')
        sp_price.mfr_suggested_retailer_price = request.POST.get('sp_retailer_price')
        sp_price.disp_actual_price = request.POST.get('display_actual_price')
        
        if special_price_idd == '0':
            sp_price.save()

        else:
            Special_price.objects.filter(id = special_price_idd).update(
                special_price_from = request.POST.get('sp_price_min_date'),
                special_price_to = request.POST.get('sp_price_max_date'),
                special_price = request.POST.get('sp_product_price'),
                special_cost = request.POST.get('sp_product_cost'),
                mfr_suggested_retailer_price = request.POST.get('sp_retailer_price'),
                disp_actual_price = request.POST.get('display_actual_price')
            )


        # ---------- Detailed Description of product --------------
        desc = Contents()
        desc.full_description = request.POST.get('product_all_details')
        desc.main_description = request.POST.get('product_main_details')
        
        if contents_idd =='0':
            desc.save()

        else:
            Contents.objects.filter(id = contents_idd).update(
                full_description = request.POST.get('product_all_details'),
                main_description = request.POST.get('product_main_details')
                
            )


        # ------ Product Quantity Advanced Inventory -----------------------------
        adv_inventory = Pro_qty_advanced_inventory()
        if request.POST.get('manage_stock') == 'on':
            adv_inventory.manage_stock = True
        if request.POST.get('out_of_stock') != None: 
            adv_inventory.out_of_stock_threshold = request.POST.get('out_of_stock')
        if request.POST.get('min_qty_cart') != None:
            adv_inventory.min_qty_allowed_in_cart = request.POST.get('min_qty_cart')
        if request.POST.get('max_qty_cart') != None:
            adv_inventory.max_qty_allowed_in_cart = request.POST.get('max_qty_cart')
        if request.POST.get('qty_decimels') == 'on':
            adv_inventory.qty_uses_decimal = True
        if request.POST.get('multi_box_ship_btn') == 'on':
            adv_inventory.allow_multi_box_of_shipping = True
        if request.POST.get('back_orders') != None:
            adv_inventory.back_orders = request.POST.get('back_orders')
        if request.POST.get('Notify_for_Quantity_Below') != None:
            adv_inventory.notify_for_qty_below = request.POST.get('Notify_for_Quantity_Below')
        if request.POST.get('enable_qty_increment') == 'on':
            adv_inventory.enable_qty_increments = True
        if request.POST.get('stock_in') == 'on':
            adv_inventory.stock_status = True
        

        if adv_inventory_idd == '0':
            adv_inventory.save()

        else:
            Pro_qty_advanced_inventory.objects.filter(id = adv_inventory_idd).update(
                    manage_stock = True,
                    out_of_stock_threshold = request.POST.get('out_of_stock'),
                    min_qty_allowed_in_cart = request.POST.get('min_qty_cart'),
                    max_qty_allowed_in_cart = request.POST.get('max_qty_cart'),
                    qty_uses_decimal = True,
                    allow_multi_box_of_shipping = True,
                    back_orders = request.POST.get('back_orders'),
                    notify_for_qty_below = request.POST.get('Notify_for_Quantity_Below'),
                    enable_qty_increments = True,
                    stock_status = True
                    )

        # ----------- Search Engine Optimization ---------------
        seo = Search_Engine_Optimization()
        seo.url_key = request.POST.get('url_key_seo')
        seo.meta_title = request.POST.get('meta_title_seo')
        seo.meta_keywords = request.POST.get('meta_keywords_seo')
        seo.meta_description = request.POST.get('meta_description_seo')
        


        if seo_idd == '0':
            seo.save()
        else:
            Search_Engine_Optimization.objects.filter(id = seo_idd).update(
                url_key = request.POST.get('url_key_seo'),
                meta_title = request.POST.get('meta_title_seo'),
                meta_keywords = request.POST.get('meta_keywords_seo'),
                meta_description = request.POST.get('meta_description_seo')
        
            )    

        # ------------ Schedule Design Update ---------------------
        schedule = Schedule_design_update()
        schedule.schedule_design_start = request.POST.get('schedule_update_start')
        schedule.schedule_design_end = request.POST.get('schedule_update_end')
        schedule.new_layout = request.POST.get('new_layout')
        schedule.new_theme = request.POST.get('new_theme')
        
        
        if schedule_design_idd == '0':    
            schedule.save()
        else:
            Schedule_design_update.objects.filter(id = schedule_design_idd).update(
                schedule_design_start = request.POST.get('schedule_update_start'),
                schedule_design_end = request.POST.get('schedule_update_end'),
                new_layout = request.POST.get('new_layout'),
                new_theme = request.POST.get('new_theme')

            )


        # ---- object of Basic fields of product---------
        product = Basic_product_form()

        product.product_name = request.POST.get('product_name')
        product.product_price = request.POST.get('product_price')
        product.tax_class = request.POST.get('tax_class')
        product.product_quantity = request.POST.get('product_quantity')
        product.length = request.POST.get('length_of_product')
        product.width = request.POST.get('width_of_product')
        product.height = request.POST.get('height_of_product')
        
        if request.POST.get('weight_of_product') != None:
            product.weight = request.POST.get('weight_of_product')

        Obj = All_categories.objects.get(id = category_idd)

        product.category = Obj
        product.visibility = request.POST.get('visibility')
        product.set_pro_new_from = request.POST.get('new_pro_min_date')
        product.set_pro_new_to = request.POST.get('new_pro_max_date')
        if request.POST.get('featured') == 'on':
            product.featured = True
        if request.POST.get('gift_option') == 'on':
            product.gift = True



        if product_id == '0':
            product.save()

        else:
            Basic_product_form.objects.filter(id = product_id).update(
                product_name = request.POST.get('product_name'),
                product_price = request.POST.get('product_price'),
                tax_class = request.POST.get('tax_class'),
                product_quantity = request.POST.get('product_quantity'),
                length = request.POST.get('length_of_product'),
                width = request.POST.get('width_of_product'),
                height = request.POST.get('height_of_product'),
                brand_name = request.POST.get('brand_name'),
                category = request.POST.get('id_of_category'),
                weight = request.POST.get('weight_of_product'),
                visibility = request.POST.get('visibility'),
                set_pro_new_from = request.POST.get('new_pro_min_date'),
                set_pro_new_to = request.POST.get('new_pro_max_date'),
                featured = True,
                gift = True
            )
        return redirect('/product_table/')       



def update_product_price(request):
    if request.method == 'POST':
        if request.POST.get('strike_end') == '' or request.POST.get('strike_start') == '': 
            r = {
                "response" : False
            }
            return JsonResponse(r)

        obj = Special_price.objects.get(id = request.POST.get('special_price_id'))

        obj.actual_per_gm = request.POST.get('actual_per_gm')
        obj.sale_per_gm = request.POST.get('sale_per_gm')
        obj.actual_total_pcs_price = request.POST.get('actual_total_pcs_price')
        obj.sale_total_pcs_price = request.POST.get('sale_total_pcs_price')
        obj.actual_pckg_cost = request.POST.get('actual_pckg_cost')
        obj.sale_pckg_cost = request.POST.get('sale_pckg_cost')
        obj.actual_parcel_cost = request.POST.get('actual_parcel_cost')
        obj.sale_parcel_cost = request.POST.get('sale_parcel_cost')
        obj.actual_other_cost = request.POST.get('actual_other_cost')
        obj.sale_other_cost = request.POST.get('sale_other_cost')
        obj.actual_total_price = request.POST.get('actual_total_price')
        obj.sale_total_price = request.POST.get('sale_total_price')
        obj.strike_price = request.POST.get('strike_price')
        obj.strike_start = request.POST.get('strike_start')
        obj.strike_end = request.POST.get('strike_end')
        obj.save()
       
        r = {
                "response" : True
            }
        return JsonResponse(r)



