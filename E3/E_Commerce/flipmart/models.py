from django.db import models
# from django.db.models.fields.files import ImageField
from E_Commerce.models import Basic_product_form

class User_registration(models.Model):
    name = models.CharField('name', max_length=30)
    email = models.CharField('email', max_length=30)
    phone_no = models.CharField('phone_no', max_length=15)
    password = models.CharField('password', max_length=15)
    age = models.CharField('age', max_length=5)
    gender = models.CharField('gender', max_length=7)
    total_price = models.BigIntegerField('total_price', null=True, default=0)
    
class Add_to_cart(models.Model):
    user_id = models.ForeignKey(User_registration, on_delete=models.CASCADE, related_name="add_to_cart")
    product_id = models.ForeignKey(Basic_product_form, on_delete=models.CASCADE, related_name='add_to_cart')
    product_quantity = models.CharField('cart_product_quantity', max_length=3)   
    product_price = models.CharField('product_price', max_length=8)
    sub_total = models.CharField('Sub_total', max_length=8)

class Review(models.Model):
    user_id = models.ForeignKey(User_registration, on_delete=models.CASCADE, related_name="review")
    product_id = models.ForeignKey(Basic_product_form, on_delete=models.CASCADE, related_name="review")
    ratings = models.CharField('ratings', max_length=1)
    text = models.CharField('text', max_length=2000)
    date = models.DateField()
    time = models.TimeField()

class Wish_list(models.Model):
    user_id = models.ForeignKey(User_registration, on_delete=models.CASCADE, related_name="wish_list")
    product_id = models.ForeignKey(Basic_product_form, on_delete=models.CASCADE, related_name="wish_list")

class Product_comparision(models.Model):
    user_id = models.ForeignKey(User_registration, on_delete=models.CASCADE, related_name="product_comparision")
    product_id = models.ForeignKey(Basic_product_form, on_delete=models.CASCADE, related_name="product_comparision")


class Address_of_customer(models.Model):
    user_id = models.ForeignKey(User_registration, on_delete=models.CASCADE, related_name="address_of_customer")
    company_name = models.CharField('company_name', max_length=40, null=True)
    country = models.CharField('country', max_length=20)
    house_no_and_street_name = models.CharField('house_no', max_length=50)
    apartment = models.CharField('apartment', max_length=40)
    city = models.CharField('city', max_length=20)
    state = models.CharField('state', max_length=20)
    pincode = models.CharField('pincode', max_length=10)
    permanent_address = models.BooleanField(default=False)

class purchase_history(models.Model):
    user_id = models.ForeignKey(User_registration, on_delete=models.CASCADE, related_name="purchase_history", default=1, null=True, blank=True)
    payment_method = models.CharField('payment_method', max_length=20, null=True, blank=True)
    order_notes = models.CharField('order_notes', max_length=200, null=True, blank=True)
    customer_addr_id = models.ForeignKey(Address_of_customer, on_delete=models.CASCADE, related_name="order_details", default=1)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

class Order_details(models.Model):
    purchase_history_id = models.ForeignKey(purchase_history, on_delete=models.CASCADE, related_name="order_details")
    product_id = models.ForeignKey(Basic_product_form, on_delete=models.CASCADE, related_name='purchase_history')
    product_quantity = models.CharField('product_quantity', max_length=5, null=True)
    onsale = models.BooleanField('on_sale', default=False)
    sub_total = models.CharField('Sub_total', max_length=8, default=0)
    price = models.CharField('price', max_length=5, null=True)
    result = models.CharField('result', max_length=5, null=True)
    
  
