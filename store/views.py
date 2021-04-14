from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Categorie
from .models.customer import Customer
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .sms import send_sms,gen_otp
# Create your views here.


random_otp=gen_otp()
msg_body= f" Your eshop OTP is {random_otp} "



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
            products=Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.gete_all_products()
        data={}
        data['products']=products
        data['categories']=categories
        print(" you are :" ,request.session.get('email'))
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
                print("current user role is ",request.session['role'] )
                user_phone="+91"+customer.phone
                send_sms(msg_body,"+17722131635", user_phone )
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
            customer= Customer(first_name=first_name,last_name=last_name, phone=phone, email=email,password=password,location=location, group_name=group_name)
            my_group1 = Group.objects.get(name=group_name) 
            print(my_group1)
            #my_group1.user_set.add(customer)
            customer.register()
            request.session['customer_id']=customer.id
            request.session['email']=customer.email
            request.session['role']=customer.group_name
            if(request.session['role']=='wholesaler'):
                return redirect('wholesaler_dashboard')
            else if(request.session['role']== 'retailer'):
                return redirect('retailer_dashboard')
            else:
                return redirect('homepage')
        else:
            data= {
            'error' : error_message,'values':value
            }
            return render(request,'signup.html' , data)

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
