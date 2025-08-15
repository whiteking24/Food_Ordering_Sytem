from django.shortcuts import render,redirect
from .models import *
from datetime import datetime 
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html', {'timestamp': datetime.now().timestamp()})


# Create your views here.
# def index(request):
#     return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if email and password:
            if not Signup.objects.filter(email=email).exists():
                # hashed_password = make_password(password)
                # Signup.objects.create(email=email, password=hashed_password)
                if password == confirmpassword:
                    Signup.objects.create(fullname=fullname,email=email,password=make_password(password),confirmpassword=make_password(confirmpassword))
                    return redirect('login')
                else:
                    messages.error(request,"Confirm Password doesnot match")
                    return redirect('signup')
            else:
                messages.success(request,'User Already exists')
                return render(request,'signup.html')
        else:
            messages.success(request,"All fields are required")
    
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            try:
                user = Signup.objects.get(email=email)
                if check_password(password , user.password):
                    return redirect('order')
                else:
                    messages.error(request,"Password Doesnt Match")
                    return redirect('login')
            except Signup.DoesNotExist:
                messages.error(request,"User does not exist")
                return redirect('login')
        else:
            messages.error(request,"All Fields Required")
            return redirect('login')        
    return render(request,'login.html')

def order(request):
    food=Products.objects.all()
    return render(request,'order.html',{'food':food})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        cemail = request.POST.get('cemail')
        queries = request.POST.get('queries')
        if cname and cemail and queries:
            Contact.objects.create(name=cname,email=cemail,queries=queries)
            return redirect('order')
        else:
            messages.error(request,"All fields required")
            return redirect('contact')
    return render(request,'contact.html')
    
def reports(request):
    data=Signup.objects.all()
    return render(request,"report.html",{'data':data})

def creports(request):
    con = Contact.objects.all()
    return render(request,'contactreport.html',{'ques': con})

def oreport(request):
    ord = OrderNow.objects.all()
    return render(request,'orderreport.html',{'ord':ord})
    
def alogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            admins = Admins.objects.get(username=username)
            if password == admins.password:
                return redirect('report')
            else:
                messages.error(request,"Incorrect Password")
                return redirect('alogin')
    return render(request,'AdminLogin.html')

def one_product(request,product_id):
    product = get_object_or_404(Products,id=product_id)
    return render(request,'one-food.html',{'product':product})

def ordernow(request,product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        fooditem = request.POST.get('fooditem')
        quantity = int(request.POST.get('quantity'))
        address = request.POST.get('address')
        # price = request.POST.get('price')
        if fullname and quantity and address:
            if Products.objects.filter(title=fooditem).exists():  
                price = quantity * product.price  
                OrderNow.objects.create(fullname=fullname,fooditem=fooditem,quantity=quantity,address=address,price=price)
                return redirect('order')
            else:
                messages.error(request,"Inavlid Food Item")
                return redirect('ordernow')
        else:
            messages.error(request,"All fields required")
            return redirect('ordernow')
    return render(request,"order-now.html",{'product':product})