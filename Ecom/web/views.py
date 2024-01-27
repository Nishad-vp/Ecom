from django.shortcuts import render,redirect,get_object_or_404
from . models import Product,Order,OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages

# Create your views here.
#Function

def index(request): 
      context={
            'prod' : Product.objects.all() ,
          
      }
      return render(request,"web/index.html", context)
def login1(request):

      if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            user = authenticate(username=username, password=password)
            if user is not None:

                  login(request, user)
                  return redirect('index')
            else:
                messages.warning(request,'invalid details')
                return redirect('login')
            
            
                  
         
           
      return render(request,"web/account/login.html")

def signup(request):
      if request.method=="POST":
            username=request.POST.get("username")
            firstname=request.POST.get("first_name")
            lastname=request.POST.get("last_name")
            email=request.POST.get("user_email")
            password=request.POST.get("pass1")
            confirm_password=request.POST.get("pass2")

            if password==confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.warning(request,"User Already Exist , Choose another username")
                elif User.objects.filter(email=email):
                    messages.warning(request,"Email Already Exist , Choose another email address")
                else:
                    customer=User.objects.create_user(username,email,password)
                    customer.first_name= firstname
                    customer.last_name=  lastname
                    customer.save()

                    messages.success(request,'Account created successfully, Please login')

                    return redirect('login')



      return render(request,"web/account/signup.html")



def logout1(request):
    logout(request)
    return render(request,"web/account/login.html")



def changepassword(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword= request.POST.get('cpassword')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                user=User.objects.get(username=username)
                user.set_password(password)
                user.save()
                messages.info(request,"Password Successfully Changed ,Please login")
                return redirect('login')
            else:
                messages.warning(request,"User doesnt exist, Create new account")
             
             

     
    return render(request,'web/account/reset.html')

     


@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart/cart_detail.html')


@login_required(login_url="login")
def checkout(request):

    return render(request, 'web/checkout.html')










@login_required(login_url="login")
def placeorder(request):
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        
        cart=request.session.get('cart')
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
    
        country=request.POST.get("country")
        address=request.POST.get("address")
        city=request.POST.get("company")
        state=request.POST.get("state")
        pin=request.POST.get("pin")
        phone=request.POST.get("phone")




        order=Order(
            user=user,
            first_name=firstname,
            last_name= lastname,
            country=country,
            address=address,
            city=city,
            state=state,
            pincode=pin,
            phone =phone,
            email =email,

           
  



        )
        order.save()

        for i in cart:
             a=float(cart[i]['price'])
             b=int(cart[i]['quantity'])
             total=a*b

             order1=OrderItem(
                order=order,
                product=cart[i]['name'],
                image=cart[i]['image'],
                price=cart[i]['price'],
                qunatity=cart[i]['quantity'],
                total=total

             
             
        )
             order1.save()
        

      
    return render(request, 'web/placeorder.html')

def success_page(request):
    return render(request,'web/success.html')
