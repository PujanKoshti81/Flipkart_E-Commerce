from django.shortcuts import redirect
from django.shortcuts import render


from . models import User_registration






def home(request):
    return render(request, 'home.html')

def details(request):
    return render(request, 'details.html')

def category(request):
    return render(request, 'category.html')

def checkout(request):
    return render(request, 'checkout.html')

def my_wishlist(request):
    return render(request, 'my_wish_list.html')

def product_comparison(request):
    return render(request, 'product_comparison.html')

def shopping_cart(request):
    return render(request, 'shopping_cart.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def track_orders(request):
    return render(request, 'track_orders.html')
    



# User registration process:
class face:
    def __a():
        print()
    def __b():
        print()
    def __c():
        print()        

def user_registration(request):
    if request.method == 'POST':
        obj = User_registration()
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.phone_no = request.POST.get('phone_no.')
        obj.password = request.POST.get('password1')
        obj.age = request.POST.get('age')
        obj.gender = request.POST.get('gender')
        obj.save()
        return redirect('home.html')



