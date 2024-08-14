from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from.models import Profile
import random
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

# Create your views here.
def signin(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        email=req.POST.get('email','')
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        address=req.POST.get('address','')
        pin=req.POST.get('pin','')
        mobile=req.POST.get('mobile','')
        image=req.FILES['image']
        req.session["username"]=username
        req.session["password"]=password
        req.session["email"]=email
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,'Username alredy exists!')
            elif User.objects.filter(email=email).exists():
                messages.info(req,'Email alredy exists!')
                return redirect('user:signin')
            else:
                user=User.objects.create_user(first_name=name,email=email,username=username,password=password)
                user.save()
                prof=Profile.objects.create(image=image,pincode=pin,mobileno=mobile,address=address,auth=user)
                prof.save()
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
def forgotpass(req):
    if req.method == "POST":
        email = req.POST.get('email', '')
        if User.objects.filter(email=email).exists():
            req.session["reset_email"] = email
            send_reset_otp(req)
            return redirect('user:password_reset_otp')
        else:
            messages.info(req, "Email not registered")
            return redirect('user:forpass')
    
    return render(req,'forgotpass.html')
def send_reset_otp(req):
    s=""
    for x in range(0,4):
        s+=str(random.randint(0,9))
    req.session["reset_otp"]=s
    send_mail("otp for signup ",s,'aswanthmpt@gmail.com',[req.session["reset_email"]],fail_silently=False)
    return None
def password_reset_otp(req):
    if req.method == "POST":
        otp = req.POST.get('otp', '')
        if otp == req.session.get("reset_otp"):
            return redirect('user:password_reset_form')
        else:
            messages.info(req, 'OTP does not match')
            # return render(req, 'password_reset_otp.html')
    return render(req, 'forotp.html')
def password_reset_form(req):
    if req.method == "POST":
        password = req.POST.get('password', '')
        cpassword = req.POST.get('cpassword', '')
        if password == cpassword:
            email = req.session.get("reset_email")
            user = User.objects.get(email=email)
            user.password = make_password(password)
            user.save()
            messages.info(req, "Password reset successfully")
            return redirect('user:login')
        else:
            messages.info(req, "Passwords do not match")
            return redirect('user:password_reset_form')
    return render(req, 'resetform.html')