from logging import LoggerAdapter
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from home.models import Product,Order
from datetime import date


# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return render(request,'index.html',{"loged_out":True})

    return render(request,'index.html')
    
def loginUser(request):

    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print (user)
            return redirect("/index")
        else:
            messages.warning(request, " wrong username or password ")
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
        logout(request)
        return redirect("/")



def signup(request):

    if request.method=="POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        
        if len(username)>15:
            messages.warning(request, " Your user name must be under 15 characters")
            return redirect("signup")

        elif not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect("signup")
        
        elif (password1!= password2):
            messages.warning(request, " Passwords do not match")
            return redirect("signup")
        
        user= User.objects.create_user(username,email, password1)
        login(request, user)
        messages.success(request, 'Your account has been created!')
        return redirect('/index')
    
    return render(request,'signup.html')

    

def products(request):
    if request.user.is_anonymous:
        return redirect('/login')
    products=Product.objects.all()
    num=len(products)
    params={'products':products,'product_count':num}
    return render(request,'products.html',params)

def cart(request):
    thank=False
    if request.method=="POST":
        cart=request.POST.get("order-info")
        cart=eval(cart)
        phone= request.POST.get("phone")
        address= request.POST.get("address")
        order=Order.objects.create(order_date=date.today(),order_phone=phone,order_address=address,customer_id=request.user.id)
        for item in cart.values():
            order.products.add(item[0])
        messages.success(request, 'Your Order has been placed!')
        thank=True
        return redirect('/cart')
        
        
    return render(request,'cart.html',{"thank":thank})

def order(request):
    return render(request,'order.html')
