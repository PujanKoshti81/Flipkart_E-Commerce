from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.shortcuts import redirect
import datetime

from . models import User_registration
from . models import Add_to_cart
from . models import Review
from . models import Wish_list
from . models import Product_comparision
from . models import Address_of_customer
from . models import Order_details
from . models import purchase_history

from E_Commerce.models import Basic_product_form
from E_Commerce.models import Special_price
from E_Commerce.models import Main_Image_and_Videos
from E_Commerce.models import Set_of_Images_and_Videos
from E_Commerce.models import Contents
from E_Commerce.models import Banners_image




#  face login =================
import cv2
import numpy as np

import logging
from E_Commerce.settings import BASE_DIR
import matplotlib.pyplot as plt

# from . import cascade as casc
from PIL import Image

from time import time
from sklearn.decomposition import PCA



# ====================== User registration process:=============================================================


def Create_dataset(user_id):

    userId = user_id
    print(cv2.__version__)
    # Detect face
    #Creating a cascade image classifier
    faceDetect = cv2.CascadeClassifier('./ml/haarcascade_frontalface_default.xml')
    #camture images from the webcam and process and detect the face
    # takes video capture id, for webcam most of the time its 0.
    cam = cv2.VideoCapture(0)

    # Our identifier
    # We will put the id here and we will store the id with a face, so that later we can identify whose face it is
    id = userId
    # Our dataset naming counter
    sampleNum = 0
    # Capturing the faces one by one and detect the faces and showing it on the window
    while(True):
        # Capturing the image
        #cam.read will return the status variable and the captured colored image
        ret, img = cam.read()
        #the returned img is a colored image but for the classifier to work we need a greyscale image
        #to convert
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #To store the faces
        #This will detect all the images in the current frame, and it will return the coordinates of the faces
        #Takes in image and some other parameter for accurate result
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        #In above 'faces' variable there can be multiple faces so we have to get each and every face and draw a rectangle around it.
        for(x,y,w,h) in faces:
            # Whenever the program captures the face, we will write that is a folder
            # Before capturing the face, we need to tell the script whose face it is
            # For that we will need an identifier, here we call it id
            # So now we captured a face, we need to write it in a file
            sampleNum = sampleNum+1
            # Saving the image dataset, but only the face part, cropping the rest
            cv2.imwrite('./ml/dataset/user.'+str(id)+'.'+str(sampleNum)+'.jpg', gray[y:y+h,x:x+w])
            # @params the initial point of the rectangle will be x,y and
            # @params end point will be x+width and y+height
            # @params along with color of the rectangle
            # @params thickness of the rectangle
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)
            # Before continuing to the next loop, I want to give it a little pause
            # waitKey of 100 millisecond
            cv2.waitKey(250)

        #Showing the image in another window
        #Creates a window with window name "Face" and with the image img
        cv2.imshow("Face",img)
        #Before closing it we need to give a wait command, otherwise the open cv wont work
        # @params with the millisecond of delay 1
        cv2.waitKey(1)
        #To get out of the loop
        if( sampleNum > 35):
            break
    #releasing the cam
    cam.release()
    # destroying all the windows
    cv2.destroyAllWindows()

    return redirect('/')




def Trainers(request):
    '''
        In trainer.py we have to get all the samples from the dataset folder,
        for the trainer to recognize which id number is for which face.

        for that we need to extract all the relative path
        i.e. dataset/user.1.1.jpg, dataset/user.1.2.jpg, dataset/user.1.3.jpg
        for this python has a library called os
    '''
    import os
    from PIL import Image

    #Creating a recognizer to train
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #Path of the samples
    path = './ml/dataset'

    # To get all the images, we need corresponing id
    def getImagesWithID(path):
        # create a list for the path for all the images that is available in the folder
        # from the path(dataset folder) this is listing all the directories and it is fetching the directories from each and every pictures
        # And putting them in 'f' and join method is appending the f(file name) to the path with the '/'
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] #concatinate the path with the image name
        #print imagePaths

        # Now, we loop all the images and store that userid and the face with different image list
        faces = []
        Ids = []
        for imagePath in imagePaths:
            # First we have to open the image then we have to convert it into numpy array
            faceImg = Image.open(imagePath).convert('L') #convert it to grayscale
            # converting the PIL image to numpy array
            # @params takes image and convertion format
            faceNp = np.array(faceImg, 'uint8')
            # Now we need to get the user id, which we can get from the name of the picture
            # for this we have to slit the path() i.e dataset/user.1.7.jpg with path splitter and then get the second part only i.e. user.1.7.jpg
            # Then we split the second part with . splitter
            # Initially in string format so hance have to convert into int format
            ID = int(os.path.split(imagePath)[-1].split('.')[1]) # -1 so that it will count from backwards and slipt the second index of the '.' Hence id
            
            # Images
            faces.append(faceNp)
            # Label
            Ids.append(ID)
            #print ID
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
        return np.array(Ids), np.array(faces)

    # Fetching ids and faces
    ids, faces = getImagesWithID(path)

    #Training the recognizer
    # For that we need face samples and corresponding labels
    recognizer.train(faces, ids)

    # Save the recogzier state so that we can access it later
    recognizer.save('./ml/recognizer/trainingData.yml')
    cv2.destroyAllWindows()

    return redirect('/')	



def Detect(request):
    Trainers(request)
    faceDetect = cv2.CascadeClassifier('./ml/haarcascade_frontalface_default.xml')


    cam = cv2.VideoCapture(0)
    # creating recognizer
    rec = cv2.face.LBPHFaceRecognizer_create()
    # loading the training data
    rec.read('./ml/recognizer/trainingData.yml')
    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    userId = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

            getId,conf = rec.predict(gray[y:y+h, x:x+w]) #This will predict the id of the face

            #print conf;
            if conf<35:
                userId = getId
                cv2.putText(img, "Detected",(x,y+h), font, 2, (0,255,0),2)
                
            else:
                cv2.putText(img, "Unknown",(x,y+h), font, 2, (0,0,255),2)

            # Printing that number below the face
            # @Prams cam image, id, location,font style, color, stroke

        cv2.imshow("Face",img)
        if(cv2.waitKey(1) == ord('q')):
            break
        elif(userId != 0):
            cv2.waitKey(1000)
            cam.release()
            cv2.destroyAllWindows()
            
            request.session['user_id'] = userId
            user = User_registration.objects.get(id=userId)
            request.session['name'] = user.name
            products = list(Basic_product_form.objects.all())

            cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
            product = {
                "products": products,
                "cart_all": cart_all,
                "total": total_amount(request.session['user_id']),
                "items":Count(request.session['user_id'])
            }

            return render(request, 'flipmart/home.html',product)

    cam.release()
    cv2.destroyAllWindows()
    return redirect('/')
        

# =============================================================================================================

def user_registration(request):
    if request.method == 'POST':
        obj = User_registration()
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.phone_no = request.POST.get('phone_no')
        # a = request.POST.get('phone_no')
        obj.password = request.POST.get('password1')
        obj.age = request.POST.get('age')
        obj.gender = request.POST.get('gender')
        obj.save()
        Create_dataset(obj.id)
        return render(request, 'flipmart/sign_in.html')

def update_status_discount():
    obj = list(Special_price.objects.all())
    for i in obj:
        print()
        if i.strike_start <= datetime.date.today() and i.strike_end >= datetime.date.today():
            
            i.sale_status = True
            i.save()
            print(i.strike_start, "yeah ooooo", i.strike_end, "status: ",i.sale_status)
        else:
            i.sale_status = False
            i.save()
            print('ohoooo   yeah ', "status: ",i.sale_status)

def total_amount(user_id):
    total = 0
    cart = list(Add_to_cart.objects.all().filter(user_id = user_id))

    for i in cart:
        pro = Basic_product_form.objects.get(id = i.product_id.id)
        if pro.special_price_id.sale_status == 1:
            total = total + int(i.product_quantity) * int(pro.special_price_id.strike_price)
        else:    
            total = total + int(i.product_quantity) * int(i.product_price)

    user = User_registration.objects.get(id=user_id)
    user.total_price = total
    user.save()    
    return total



def flipmart_home(request):
    update_status_discount()    
    products = list(Basic_product_form.objects.all())
    banners = list(Banners_image.objects.all().filter(status = 1))
    try:
        cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    except KeyError:
        return  render(request,'flipmart/sign_in.html')

    sale_products = list(Basic_product_form.objects.all().filter(special_price_id__sale_status = 1))
    # actual_products = list(Basic_product_form.objects.all().filter(special_price_id__sale_status = 0))


    product = {
        "products": products,
        "sale_products" : sale_products,
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id']),
        "banners":banners
    }
    return render(request, 'flipmart/home.html', product)



def shop(request):
    update_status_discount()    
    products = list(Basic_product_form.objects.all())
    try:
        cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    except KeyError:
        return  render(request,'flipmart/sign_in.html')

  

    product = {
        "products": products,
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id']),
    }
    return render(request,'flipmart/shop.html',product)



def update_cart(request):
    update_status_discount()    
    if request.method == 'GET':
        cart = Add_to_cart.objects.get(user_id= request.session['user_id'],product_id = request.GET.get('id'))
        cart.product_quantity =  request.GET.get('quantity')
        
        product = Basic_product_form.objects.get(id = request.GET.get('id'))
     
        if product.special_price_id.sale_status == 1:
            cart.sub_total = int(product.special_price_id.strike_price) * int(request.GET.get('quantity'))
        else:
            # else cart.special_price_id.sale_status == 0:
            cart.sub_total = int(cart.product_price) * int(request.GET.get('quantity'))
        cart.save()
        sub = {
            "sub_total":cart.sub_total,
            "id":request.GET.get('id'),
            "grand_total":total_amount(request.session['user_id'])
        }
        return JsonResponse(sub)

def shopping_cart(request):
    update_status_discount()    
    user = User_registration.objects.get(id=request.session['user_id'])
    reviews = list(Review.objects.all().filter(user_id=request.session['user_id']))
    cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))

    for i in cart_all:
        pro = Basic_product_form.objects.get(id=i.product_id.id)
        if pro.special_price_id.sale_status == 1:
            i.sub_total = int(i.product_quantity) * int(pro.special_price_id.strike_price)
        else:
            i.sub_total = int(i.product_quantity) * int(i.product_price)
        i.save()

    product = {
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id']),
        "total_amount":total_amount(request.session['user_id'])
        # "reviews"
    }
    return render(request, 'flipmart/shopping_cart.html',product)



def category(request):
    update_status_discount()    
    products = list(Basic_product_form.objects.all())
    
    cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    product = {
        "products": products,
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id'])
    }
    return render(request, 'flipmart/category.html',product)


def checkout(request):
    products = list(Basic_product_form.objects.all())
    cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    user = User_registration.objects.get(id = request.session['user_id'])
    product = {
            "products": products,
            "cart_all": cart_all,
            "total": total_amount(request.session['user_id']),
            "items":Count(request.session['user_id']),
            "user":user,
        }
    try:
        address = Address_of_customer.objects.get(user_id=request.session['user_id'], permanent_address=True)
        product["address"] = address

    except Address_of_customer.DoesNotExist:
        pass

    return render(request, 'flipmart/checkout.html',product)


def place_order(request):
    update_status_discount()    
    if request.method == 'POST':
        user = User_registration.objects.get(id= request.session['user_id'])
        
        purchase_hist = purchase_history()
        purchase_hist.user_id = user
        purchase_hist.customer_addr_id = address
        purchase_hist.order_notes = request.POST.get('order_comments')
        purchase_hist.payment_method = request.POST.get('payment_method')
        purchase_hist.save()

        products = Add_to_cart.objects.all().filter(user_id = request.session['user_id'])
        
        for i in products:
            order_history = Order_details()
            order_history.user_id = user
            order_history.product_id = i.product_id
            order_history.purchase_history_id = purchase_hist
            order_history.product_quantity = i.product_quantity
            if i.product_id.special_price_id.sale_status == 1:
                order_history.onsale = True
                order_history.price = i.product_id.special_price_id.strike_price
                order_history.result = int(i.product_id.special_price_id.strike_price) - int(i.product_id.special_price_id.sale_total_price)
            else:
                order_history.onsale = False
                order_history.price = i.product_id.product_price
                order_history.result = int(i.product_id.product_price) - int(i.product_id.special_price_id.actual_total_price)
            order_history.sub_total = i.sub_total
             
            order_history.save()


        address = Address_of_customer()
        address.user_id = user
        address.company_name = request.POST.get('billing_company')
        address.country = request.POST.get('billing_country')
        address.house_no_and_street_name = request.POST.get('billing_address_1')
        address.apartment = request.POST.get('billing_address_2')
        address.city = request.POST.get('billing_city')
        address.state = request.POST.get('billing_state')
        address.pincode = request.POST.get('billing_postcode')
        if 'on' != request.POST.get('base_add'):
            address.permanent_address = False
        else:    
            address.permanent_address = True
        
        address.save()


        products = list(Basic_product_form.objects.all())
        
        cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
        product = {
            "products": products,
            "cart_all": cart_all,
            "total": total_amount(request.session['user_id']),
            "items":Count(request.session['user_id'])
        }
        return render(request, 'flipmart/home.html', product)



def my_wishlist(request):
    update_status_discount()    
    products = list(Basic_product_form.objects.all())
    cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    wish = list(Wish_list.objects.all().filter(user_id = request.session['user_id']))
    product = {
        "wishlist":wish,
        "products": products,
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id'])
    }
    return render(request, 'flipmart/my_wish_list.html',product)


def product_comparison(request):
    update_status_discount()    
    products = list(Basic_product_form.objects.all())
    cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))

    compare = list(Product_comparision.objects.all().filter(user_id=request.session['user_id']))
    product = {
        "compare":compare,
        "products": products,
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id'])
    }
    return render(request, 'flipmart/product_comparison.html',product)

def del_pro_compare(request):
    if request.method == 'GET':
        product = Product_comparision.objects.get(product_id = request.GET.get('product_id'),user_id = request.session['user_id'])
        product.delete()
        w = {
            "done":True,
            "response":"Item removed from comparison."
        }
        return JsonResponse(w)


def sign_in(request):
    update_status_discount()    
    # products = list(Basic_product_form.objects.all())
    
    # cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    # product = {
    #     "products": products,
    #     "cart_all": cart_all,
    #     "total": total_amount(request.session['user_id']),
    #     "items":Count(request.session['user_id'])
    # }
    return render(request, 'flipmart/sign_in.html')


def track_orders(request):
    products = list(Basic_product_form.objects.all())
    
    cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    product = {
        "products": products,
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id'])
    }
    return render(request, 'flipmart/track_orders.html',product)


def Count(user_id):
    count = 0
    cart = list(Add_to_cart.objects.all().filter(user_id = user_id).values())

    for i in cart:
        count = count + int(i['product_quantity']) * 1
    return count



def add_to_cart(request):
    update_status_discount()    
    if request.method == 'GET':
        cart = Add_to_cart()
        product = Basic_product_form.objects.get(id=request.GET.get('product_id'))
        user = User_registration.objects.get(id=request.GET.get('user_id'))
        
        try:
            in_cart = Add_to_cart.objects.get(product_id=product.id,user_id=user.id)
            if request.GET.get('quantity') == None:    
                in_cart.product_quantity = int(in_cart.product_quantity) + 1

                if product.special_price_id.sale_status == 1:
                    in_cart.sub_total = (int(in_cart.product_quantity) + 1) * int(product.special_price_id.strike_price)
                else:
                    in_cart.sub_total = (int(in_cart.product_quantity) + 1) * int(in_cart.product_price)
            else:
                in_cart.product_quantity = int(in_cart.product_quantity) + int(request.GET.get('quantity'))

                if product.special_price_id.sale_status == 1:
                    in_cart.sub_total = (int(in_cart.product_quantity) + int(request.GET.get('quantity'))) * int(product.special_price_id.strike_price)
                else:    
                    in_cart.sub_total = (int(in_cart.product_quantity) + int(request.GET.get('quantity'))) * int(in_cart.product_price)
            in_cart.user_id = user
            in_cart.save()

        except Add_to_cart.DoesNotExist:
            cart.product_id = product
            cart.product_price = product.product_price
            if request.GET.get('quantity') == None:
                cart.product_quantity = 1
                if product.special_price_id.sale_status == 1:
                    in_cart.sub_total = (int(in_cart.product_quantity) + 1) * int(product.special_price_id.strike_price)
                else:
                    cart.sub_total = (int(cart.product_quantity) + 1) * int(cart.product_price)
            else:
                cart.product_quantity = request.GET.get('quantity')
                
                if product.special_price_id.sale_status == 1:
                    in_cart.sub_total = (int(in_cart.product_quantity) + int(request.GET.get('quantity'))) * int(product.special_price_id.strike_price)
                else:
                    cart.sub_total = (int(cart.product_quantity) + int(request.GET.get('quantity'))) * int(cart.product_price)
            cart.user_id = user
            cart.save()

        user.total_price = total_amount(request.GET.get('user_id'))
        user.save()
        cart_all = list(Add_to_cart.objects.all().filter(user_id=user.id))
        total = user.total_price
  
        response = {
            "cart_all": cart_all,
            "Total_price": total,
            "items": Count(request.GET.get('user_id')),
            
        }
        return JsonResponse(response)


def del_pro_wishlist(request):
    update_status_discount()    
    if request.method == 'GET':
        product = Wish_list.objects.get(product_id = request.GET.get('product_id'),user_id = request.session['user_id'])
        product.delete()
        # products = list(Add_to_cart.objects.all().filter(user_id = request.session['user_id']).values())
        w = {
            "done":True
        }
        return JsonResponse(w)


def delete_product_cart(request):
    update_status_discount()    
    if request.method == 'GET':
        product = Add_to_cart.objects.get(product_id = request.GET.get('p_id'),user_id = request.session['user_id'])
        product.delete()
        products = list(Add_to_cart.objects.all().filter(user_id = request.session['user_id']).values())
        # main_images = list(Main_Image_and_Videos.objects.all().filter(product_id=))
        cartt = {
            "cart" : products,
            "done":True
        }
        return JsonResponse(cartt)

def Login_check(request):
    update_status_discount()    
    if request.method == 'POST':
        products = list(Basic_product_form.objects.all())
        email = request.POST.get('email')
        password = request.POST.get('password')

        try : 
            user = User_registration.objects.get(email = email, password = password)
            # cart_all = list(Add_to_cart.objects.all().filter(user_id=user.id))
        
            # total = user.total_price
            # items = Count(user.id)
            # product = {
            #     "products": products,
            #     "cart_all": cart_all,
            #     "total":total,
            #     "items":items
            # }

            # request.session['cart_all'] = cart_all
            # request.session['total'] = total
            # request.session['products'] = product

        except User_registration.DoesNotExist :
            user = None

        if user == None:
            return  render(request,'flipmart/sign_in.html')

        else : 
            request.session['name'] = user.name
            request.session['user_id']  = user.id
            return flipmart_home(request)
            # return render(request,'flipmart/home.html',product)  
      
    

def logout_session(request):
    Session.objects.all().delete()
    return render (request,'flipmart/sign_in.html')  


                    


def rating_avg(product_id):
    sets = list(Review.objects.all().filter(product_id = product_id))
    num = len(sets)
    products = Basic_product_form.objects.get(id = product_id)
    products.review_count = int(len(sets)) 
    products.save()
    
    if num == 0:
        return "No Ratings"
    else:    
        total = 0
        for i in sets:
            total = total + int(i.ratings)
        return int(total/num)

def details(request):
    update_status_discount()    
    products = list(Basic_product_form.objects.all())
    product_details = Basic_product_form.objects.get(id = request.GET.get("product_id"))
    desc = product_details.contents_id
    set_of_img = list(Set_of_Images_and_Videos.objects.all().filter(main_img_id = product_details.main_image_id).values())
    cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
    reviews = list(Review.objects.all().filter(product_id=request.GET.get("product_id")))
    product = {
        "products": products,
        "cart_all": cart_all,
        "total": total_amount(request.session['user_id']),
        "items":Count(request.session['user_id']),
        "details": product_details,
        "set_of_img" : set_of_img,
        "desc":desc,
        "reviews":reviews,
        "review_count":len(reviews),
        "avg_ratings":rating_avg(request.GET.get("product_id"))
    }
    return render(request, 'flipmart/details.html',product)

def review(request):
    if request.method == 'POST':
        if "" == request.POST.get('ratings')  :
            res = {
                "done":False
            }
            return JsonResponse(res)
        else:
            RR = Review()
            RR.user_id = User_registration.objects.get(id = request.POST.get('user_id'))
            RR.product_id = Basic_product_form.objects.get(id = request.POST.get('product_id'))
            RR.ratings = request.POST.get('ratings')
            RR.text = request.POST.get('text')
            RR.date = datetime.datetime.now().date()
            RR.time = datetime.datetime.now().time()
            RR.save()
            pro = list(Basic_product_form.objects.all())
            for i in pro:
                i.avg_review = rating_avg(i.id)
                i.save()
            res = {
                "done":True
            }
            return JsonResponse(res)


def wish_list(request):
    update_status_discount()    
    if request.method == 'GET':
        try:
            wish = Wish_list.objects.get(user_id = request.session['user_id'], product_id = request.GET.get('product_id'))
            r = {
                "done":True,
                "response":"Already exist in your wishlist"
            }
            return JsonResponse(r)
        except Wish_list.DoesNotExist:
            wish = Wish_list()
            user = User_registration.objects.get(id=request.session['user_id'])
            wish.user_id = user
            product = Basic_product_form.objects.get(id=request.GET.get('product_id'))
            wish.product_id = product
            wish.save()
            r = {
                "done":True,
                "response":"Item saved in your wishlist!!!"
            }
            return JsonResponse(r)

def compare(request):
    update_status_discount()    
    if request.method == 'GET':
        try:
            compare = Product_comparision.objects.get(user_id = request.session['user_id'], product_id = request.GET.get('product_id'))
            r = {
                "done":True,
                "response":"Already Comparing..."
            }
            return JsonResponse(r)
        except Product_comparision.DoesNotExist:
            compare = Product_comparision()
            user = User_registration.objects.get(id=request.session['user_id'])
            compare.user_id = user
            product = Basic_product_form.objects.get(id=request.GET.get('product_id'))
            compare.product_id = product
            compare.save()
            r = {
                "done":True,
                "response":"Item set for comparison !!!"
            }
            return JsonResponse(r)


