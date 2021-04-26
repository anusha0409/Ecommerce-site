from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Categorie
from .models.customer import Customer
from .models.item import Item
from .models.orders import Order
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .sms import send_sms,gen_otp
from django.views.decorators.csrf import csrf_protect
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import random


# Create your views here.


random_otp=gen_otp()
msg_body= f" Your eshop OTP is {random_otp} "
msg_feedback="Dear customer, your order was successfully delivered today. Kindly provide your feedback on Apni Dukan's site. Keep shopping with us!"

delivery_men=["Vimal Prakash , 9876543211" , "Bharat Solanki , 9897001112" , "Rakesh Singh , 9897119900" , "Sher Singh , 9090887711 "]

def payment(request):
    return render(request, 'payment.html')

def signup(request):
    if(request.method =='GET'):
        return render(request , 'signup.html')
    if(request.method=='POST'):
        postData=request.POST
        first_name=postData.get("firstname")
        last_name=postData.get("lastname")
        phone=postData.get("phone")
        email=postData.get("email")
        password=postData.get('password')
        retypepassword=postData.get('retypepassword')
        location=postData.get('location')
        group_name=postData.get('group_name')
        print("group name is   ",group_name)
        #validation
        error_message = None
        value={
            "first_name": first_name,
            "last_name":last_name, 
            "phone":phone,
             "email": email,
             "location":location
        }
        if(not first_name ):
            error_message="First Name Required !"
        if(not last_name):
            error_message="Last Name Required ! "
        if(not(password == retypepassword)):
            error_message= "Password does not match ! "
        if(not phone or not(len(phone)==10)):
            error_message="Invalid number !"
        


        #created object
        if not error_message:
            customer= Customer(first_name=first_name,last_name=last_name, phone=phone, email=email,password=password,location=location,group_name=group_name)
            my_group1 = Group.objects.get(name=my_group) 
            print(my_group1)
            my_group1.user_set.add(customer)
            customer.register()
            return redirect('homepage')
        else:
            data= {
            'error' : error_message,'values':value
            }
            return render(request,'signup.html' , data)
        


def otp_verify(request):
    if(request.method =='GET'):
        return render(request , 'otp_verify.html')
    else:
        postData=request.POST
        otp=postData.get("otp")
        if otp == random_otp:
                if(request.session['role']=='wholesaler'):
                    return redirect('wholesaler_dashboard')
                elif(request.session['role']== 'retailer'):
                    return redirect('retailer_dashboard')
                else:
                    return redirect('homepage')
        else:
            return render(request,'otp_verify.html')



def logout(request):
    request.session.clear()
    return redirect('login')

class Index(View):
    def get(self,request):
        products = None
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}

        categories=Categorie.get_all_categories()
        categoryID=request.GET.get('category')
        if categoryID:
            products=Product.get_by_category_and_role("retailer",categoryID)
        else:
            products = Product.get_all_products_by_roleOfSeller("retailer")
        data={}
        data['products']=products
        data['categories']=categories
        #print(" you are :" ,request.session.get('email'))
        return render(request , 'index.html' , data)
        
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if(quantity<=1):
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1

                else:
                    cart[product]=1+quantity
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        
        
        request.session['cart']=cart
        return redirect('homepage')
        


class Login(View):
    def get(self, request):
        return  render(request,'login.html')
    
    def post(self, request):
        email=request.POST.get("email")
        mobile=request.POST.get("phone")
        password=request.POST.get("password")
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            if not(password==customer.password):
                error_message="Invalid password"
            else:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email
                request.session['role']=customer.group_name
                request.session['user_name']=customer.first_name
                print("current user role is ",request.session['role'] )
                user_phone="+91"+customer.phone
                send_sms(msg_body,"+17722131635", user_phone )
                print(msg_body)
                return redirect('otp_verification')

        else:
            error_message ="No such user exists. Kindly check the email or signup"   
        return render(request, 'login.html', {"error" : error_message })

class Signup(View):
    def get(self,request):
        return render(request , 'signup.html')
    def post(self,request):
        postData=request.POST
        first_name=postData.get("firstname")
        last_name=postData.get("lastname")
        phone=postData.get("phone")
        email=postData.get("email")
        password=postData.get('password')
        retypepassword=postData.get('retypepassword')
        location=postData.get('location')
        group_name=postData.get('group_name')
        if('latitude' in self.request.session):
            latitude=self.request.session['latitude']
            longitude=request.session['longitude']
        print("group name is   ",group_name)
        #validation
        error_message = None
        value={
            "first_name": first_name,
            "last_name":last_name, 
            "phone":phone,
             "email": email,
             "location":location
        }
        if(not first_name ):
            error_message="First Name Required !"
        if(not last_name):
            error_message="Last Name Required ! "
        if(not(password == retypepassword)):
            error_message= "Password does not match ! "
        if(not phone or not(len(phone)==10)):
            error_message="Invalid number !"
        


        #created object
        if not error_message:
            customer= Customer(first_name=first_name,last_name=last_name, phone=phone, email=email,password=password,location=location, group_name=group_name, latitude=latitude, longitude=longitude)
            my_group1 = Group.objects.get(name=group_name) 
            print(my_group1)
            #my_group1.user_set.add(customer)
            customer.register()
            request.session['customer_id']=customer.id
            request.session['email']=customer.email
            request.session['role']=customer.group_name
            request.session['user_name']=customer.first_name
            if(request.session['role']=='wholesaler'):
                return redirect('wholesaler_dashboard')
            elif(request.session['role']== 'retailer'):
                return redirect('retailer_dashboard')
            else:
                return redirect('homepage')
        else:
            data= {
            'error' : error_message,'values':value
            }
            return render(request,'signup.html' , data)

class Cart(View):
    #@method_decorator(auth_middleware)
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        customers=Customer.get_customer_by_role('retailer')
        print("latitude    ", "longitude")
        latitudes=[]
        longitudes=[]
        for customer in customers:
            latitudes.append(customer.latitude)
            longitudes.append(customer.longitude)
            print(customer.latitude,customer.longitude)
      
        
        return render(request , 'cart.html' , {'products' : products, 'customers' : customers, } )

class CartRetailer(View):
    #@method_decorator(auth_middleware)
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart_retailer.html' , {'products' : products} )


class CheckOut(View):
    def post(self, request):
        mode=request.POST.get('mode')
        print(mode)
        if(mode =="online"):
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
            customer = request.session.get('customer_id')


            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))
            #print(address, phone, customer, cart, products)

            for product in products:
                order = Order(customer=Customer(id=customer),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                order.placeOrder()
            request.session['cart'] = {}
            if(request.session['role']=='retailer'): 
                return redirect('cart_retailer')
            else:
                return redirect('cart')
        elif(mode =="offline"):
            date=request.POST.get('date')
            time=request.POST.get("time")
            print(date, time)
            customer = request.session.get('customer_id')
            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))
            for product in products:
                #print(cart.get(str(product.id)))
                order = Order(customer=Customer(id=customer),
                            product=product,
                            price=product.price,
                            quantity=cart.get(str(product.id)),
                            date_of_delivery=date,
                            time_pickup=time,
                            mode="Offline"
                            )
                order.placeOrder()
            request.session['cart'] = {}
            if(request.session['role']=='retailer'): 
                return redirect('cart_retailer')
            else:
                return redirect('cart')



class OrderView(View):
    def get(self , request ):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})

class Locate(View):
    def get(self ,request):
        return render(request,"locate.html")


class orders_given_by_retailer(View):
     def get(self , request ):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        #print(orders)
        return render(request , 'orders_given_by_retailer.html'  , {'orders' : orders})



class Wholesaler_dashboard(View):
    def get(self ,request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_seller(customer)
        #print(orders)
        if(request.session['role']=='wholesaler'):
            return render(request,'wholesaler_dashboard.html',{"orders": orders})
        elif(request.session['role']=='retailer'):
            return render(request,'orders_recieved_by_retailer.html',{"orders": orders})



    

class view_order(View):
    def get(self,request):
        #print(request.GET)
        order_id=request.GET.get('order')
        order=Order.objects.get(id=order_id)
        print(order.order_status)
        print(order.mode)
        if(request.session['role']=='wholesaler'):
            return render(request,'view_order.html',{"order": order})
        elif(request.session['role']=='retailer'):
            return render(request,'view_order2.html',{"order": order})

    

    def post(self,request):
        order_id=request.POST.get('order')
        status=request.POST.get('order_status')
        order=Order.objects.get(id=order_id)
        quant=order.quantity
        old_status=order.order_status
        new_status=status
        if(old_status=="Order Placed" and (new_status== 'Order Dispatched' or new_status == 'In transit' or new_status=='Delivered')):
            product_id=order.product.id
            obj = Product.objects.get(id=product_id)
            obj.quantity=obj.quantity-quant
            obj.save()
        if(new_status == 'In transit'):
            l=len(delivery_men)
            i=random.randint(0,l-1)
            order.delivery_person_details=delivery_men[i]
            order.save()
        if(new_status =='Delivered'):
            customer_id=order.customer.id
            obj = Customer.objects.get(id=customer_id)
            phone=obj.phone
            user_phone="+91"+phone
            send_sms(msg_feedback,"+17722131635", user_phone )
            print(msg_feedback)
        order.order_status=status
        print(order.order_status)
        order.save()
        if(request.session['role']=='wholesaler'):
            return render(request,'view_order.html',{"order": order})
        elif(request.session['role']=='retailer'):
            return render(request,'view_order2.html',{"order": order})


class feedback(View):
    def get(self,request):
        order_id=request.GET.get('order')
        order=Order.objects.get(id=order_id)
        if(request.session['role']=='retailer'):
            return render(request,'feedback_retailer.html',{"order": order})
        elif(request.session['role']=='customer'):
            return render(request,'feedback_customer.html',{"order": order})
    def post(self,request):
        order_id=request.POST.get('order')
        feedback=request.POST.get('feedback')
        order=Order.objects.get(id=order_id)
        order.feedback=feedback
        order.save()
        if(request.session['role']=='retailer'):
            return redirect('orders_given_by_retailer')
        elif(request.session['role']=='customer'):
            return redirect("orders")



@csrf_protect
def my_view_that_updates_pieFact(request):
    if request.method == 'POST':
        print(request.POST)
        if 'latitude' in request.POST:
            # doSomething with pieFact here...
            print("HIIIIIIIIIIII")
            print(request.POST['latitude'])
            request.session['longitude']=request.POST['longitude']
            request.session['latitude']=request.POST['latitude']
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')




class add_products(View):
    def get(self,request):
        categories=Categorie.get_all_categories()
        return render(request, 'add_products.html',{'categories': categories})
    
    def post(self,request):
        postData=request.POST
        name=postData.get("name")
        price=postData.get("price")
        quantity=postData.get("quantity")
        description=postData.get("description")
        image_name= request.FILES['img']
        customer = request.session.get('customer_id')
        fs = FileSystemStorage()
        filename = fs.save(image_name.name, image_name)
        print(image_name)
        category_id=postData.get("category")
        seller_id=request.session["customer_id"]
        seller=Customer.get_customer_by_id(seller_id)
        category=Categorie.get_category_by_id(category_id)
        product=Product(seller=Customer(id=customer),name=name,price=price,category=category,description=description,image=filename,quantity=quantity)#,seller = seller)
        product.save_product()
        return HttpResponseRedirect(self.request.path_info) 


class notif(View):
    def get(self,request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_seller(customer)
        if (request.session['role']=='wholesaler'):
            return render(request,'notifications_wholesaler.html',{"orders": orders})
        if (request.session['role']=='retailer'):
            return render(request,'notifications_retailer.html',{"orders": orders})


class add_products_retailer(View):
    def get(self,request):
        categories=Categorie.get_all_categories()
        return render(request, 'add_products_retailer.html',{'categories': categories})
    
    def post(self,request):
        postData=request.POST
        name=postData.get("name")
        price=postData.get("price")
        quantity=postData.get("quantity")
        description=postData.get("description")
        image_name= request.FILES['img']
        customer = request.session.get('customer_id')
        fs = FileSystemStorage()
        filename = fs.save(image_name.name, image_name)
        print(image_name)
        category_id=postData.get("category")
        seller_id=request.session["customer_id"]
        seller=Customer.get_customer_by_id(seller_id)
        category=Categorie.get_category_by_id(category_id)
        product=Product(seller=Customer(id=customer),name=name,price=price,category=category,description=description,image=filename,quantity=quantity)#,seller = seller)
        product.save_product()
        return HttpResponseRedirect(self.request.path_info) 


class ProductsView(View):
    def get(self , request ):
        customer = request.session.get('customer_id')
        products = Product.get_products_by_seller(customer)
        print(products)
        return render(request , 'my_products.html'  , {'products' : products})

class ProductsRetailerView(View):
    def get(self , request ):
        customer = request.session.get('customer_id')
        products = Product.get_products_by_seller(customer)
        print(products)
        return render(request , 'my_products_retailer.html'  , {'products' : products})
        
class Retailer_dashboard(View):
    def get(self ,request):
        #return  render(request,'retailer_dashboard.html')
        products = None
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}

        categories=Categorie.get_all_categories()
        categoryID=request.GET.get('category')
        if categoryID:
            products=Product.get_by_category_and_role("wholesaler",categoryID)
        else:
            products = Product.get_all_products_by_roleOfSeller("wholesaler")
        data={}
        data['products']=products
        data['categories']=categories
        #print(" you are :" ,request.session.get('email'))
        return render(request , 'retailer_dashboard.html' , data)
        
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if(quantity<=1):
                        cart.pop(product)
                    else:
                        cart[product]=quantity-10

                else:
                    cart[product]=10+quantity
            else:
                cart[product]=10
        else:
            cart={}
            cart[product]=10
        
        
        request.session['cart']=cart
        return redirect('retailer_dashboard')