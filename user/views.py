from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signin(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        email=req.POST.get('email','')
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,'Username alredy exists!')
            elif User.objects.filter(email=email).exists():
                messages.info(req,'Email alredy exists!')
                return redirect('user:signin')
            else:
                user=User.objects.create_user(first_name=name,email=email,username=username,password=password)
                user.save()
                return redirect('user:login')
        else:
            messages.info(req,'password doesnot match')
            return redirect('user:signin')
    return render(req,'signin.html')
def login_u(req):
    if req.method=='POST':
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            
            auth.login(req,user)
           
            req.session['user']=str(user)
            
            return redirect('main:home')
        else:
            messages.info(req,'Inavalid Details')
            return redirect('user:login')
    
    return render(req,'login.html')
def logout_u(req):
    auth.logout(req)
    req.session.flush()
    return redirect('main:home')