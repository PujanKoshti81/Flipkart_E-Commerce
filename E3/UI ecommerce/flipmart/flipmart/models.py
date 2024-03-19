from django.db import models
from django.db.models.fields.files import ImageField



class User_registration(models.Model):
	name = models.CharField('name', max_length=30)
	email = models.CharField('email',max_length=30)
	phone_no = models.CharField('phone_no', max_length=15)
	password = models.CharField('password', max_length=15)
	age = models.CharField('age', max_length=5)
	gender = models.CharField('gender', max_length=7)










###########  E_Commerce Classes ################

class Category_level_1(models.Model):
	category_name = models.CharField('category_name',max_length=30)

class Category_level_2(models.Model):
	category_L2_name = models.CharField('category_L2_name',max_length=30)
	CL1_id = models.ForeignKey(Category_level_1, on_delete=models.CASCADE)

class Category_level_3(models.Model):
	category_L3_name = models.CharField('category_L3_name',max_length=30)
	CL2_id = models.ForeignKey(Category_level_2, on_delete=models.CASCADE)	

class Category_level_4(models.Model):
	category_L4_name = models.CharField('category_L4_name',max_length=30)
	CL3_id = models.ForeignKey(Category_level_3, on_delete=models.CASCADE)

class Category_level_5(models.Model):
	category_L5_name = models.CharField('category_L5_name',max_length=30)
	CL4_id = models.ForeignKey(Category_level_4, on_delete=models.CASCADE)	

class All_categories(models.Model):
	category_level_1 = models.CharField('category_level_1',max_length=30)
	category_level_2 = models.CharField('category_level_2',max_length=30)
	category_level_3 = models.CharField('category_level_3',max_length=30)
	category_level_4 = models.CharField('category_level_4',max_length=30)
	category_level_5 = models.CharField('category_level_5',max_length=30)	

class Color_theme(models.Model):
	header = models.CharField('Header',max_length=10)
	sidebar = models.CharField('Sidebar',max_length=10)
	background_color = models.CharField('Background_color',max_length=10)	

class Banners_image(models.Model):
	image = models.FileField(upload_to='banner_image/')	
	status = models.BooleanField(default=False)

# ----- PRODUCT FORM TABLES-------------------------------------------


class Special_price(models.Model):
	# special_price_from = models.DateField()
	# special_price_to = models.DateField()
	special_price_from = models.CharField('special_price_from',max_length=20)
	special_price_to = models.CharField('special_price_to',max_length=20)	
	special_price = models.CharField('special_price',max_length=10)
	special_cost = models.CharField('special_cost',max_length=10)
	mfr_suggested_retailer_price = models.CharField('mfr_suggested_retailer_price',max_length=10)
	disp_actual_price = models.CharField('disp_actual_price',max_length=30)

class Pro_qty_advanced_inventory(models.Model):
	manage_stock = models.BooleanField(default=False)
	out_of_stock_threshold = models.CharField('out_of_stock_threshold',max_length=10)
	min_qty_allowed_in_cart = models.CharField('min_qty_allowed_in_cart',max_length=10)
	max_qty_allowed_in_cart = models.CharField('max_qty_allowed_in_cart',max_length=10)
	qty_uses_decimal = models.BooleanField(default=False)
	allow_multi_box_of_shipping = models.BooleanField(default=False)
	back_orders  = models.CharField('back_orders',max_length=40)
	notify_for_qty_below = models.CharField('notify_for_qty_below',max_length=10)
	enable_qty_increments = models.BooleanField(default=False)
	stock_status = models.BooleanField(default=False)

class Contents(models.Model):
	full_description = models.CharField('full_description',max_length=300)
	main_description = 	models.CharField('main_description',max_length=100)

class Main_Image_and_Videos(models.Model):
	main_image = models.FileField(upload_to='product_images/')
	thumbnail = models.FileField(upload_to='product_thumbanails/')
	url_of_videos = models.FileField(upload_to='product_videos/')

class Set_of_Images_and_Videos(models.Model):
	main_img_id = models.ForeignKey(Main_Image_and_Videos,on_delete=models.CASCADE)
	url_of_images = models.FileField(upload_to='set_of_product_images/')
	# url_of_videos = models.FileField(upload_to='set_of_product_videos/')

class Search_Engine_Optimization(models.Model):
	url_key = models.CharField('URL_KEY',max_length=40)
	meta_title = models.CharField('meta_title',max_length=50)
	meta_keywords = models.CharField('meta_keywords',max_length=50)
	meta_description = models.CharField('meta_description',max_length=200)


class Schedule_design_update(models.Model):
	# schedule_design_start = models.DateField()	
	# schedule_design_end = models.DateField()
	schedule_design_start = models.CharField('schedule_design_start',max_length=20)	
	schedule_design_end = models.CharField('schedule_design_end',max_length=20)
	new_theme = models.CharField('new_theme',max_length=20)
	new_layout = models.CharField('new_layout',max_length=20)


# ---------- OPTIONAL ------------------------- 
# class Variant_products(models.Model):
# 	color_of_product = models.CharField('colour_of_product',max_length=10)
# 	size = models.CharField('size_of_colour_product',max_length=10)
# 	price =  models.CharField('colour_of_product',max_length=10)


class Basic_product_form(models.Model):
	special_price_id = models.ForeignKey(Special_price,on_delete=models.CASCADE)
	adv_inventory_id = models.ForeignKey(Pro_qty_advanced_inventory,on_delete=models.CASCADE)
	contents_id = models.ForeignKey(Contents,on_delete=models.CASCADE)
	main_image_id = models.ForeignKey(Main_Image_and_Videos,on_delete=models.CASCADE)
	seo_id = models.ForeignKey(Search_Engine_Optimization,on_delete=models.CASCADE)
	schedule_design_id = models.ForeignKey(Schedule_design_update,on_delete=models.CASCADE)
	# variant_products_id = models.ForeignKey(Variant_products,on_delete=models.CASCADE)

	product_name = models.CharField('product_name',max_length=50)
	product_price = models.CharField('product_price',max_length=10)
	tax_class = models.CharField('tax_class',max_length=20)
	product_quantity = models.CharField('product_quantity',max_length=10)
	length = models.CharField('length',max_length=10)
	width = models.CharField('width',max_length=10)
	height = models.CharField('height',max_length=10)
	weight = models.CharField('weight',max_length=10)
	brand_name = models.CharField('brand_name',max_length=30)
	# category id will appear here---------------------------------------
	category = models.ForeignKey(All_categories,on_delete=models.CASCADE)
	# and it will link this table to the category---------------------------

	visibility = models.CharField('visibility',max_length=30)
	# set_pro_new_from = models.DateField()
	# set_pro_new_to = models.DateField()
	set_pro_new_from = models.CharField('set_pro_new_from',max_length=20)
	set_pro_new_to = models.CharField('set_pro_new_to',max_length=20)
	featured = models.BooleanField(default=False)
	gift = models.BooleanField(default=False)

	# image = models.FileField(upload_to='product_images/')	
