from audioop import reverse
from email import message
import email
import math
from django.contrib import messages
import random
from django.http import HttpResponse
from django.shortcuts import redirect, render

# # Create your views here.
from .models import Register,Otp
from .forms import SignupForm
# from .models import Otp,Register
from django.core.mail import send_mail

def register(request):
     if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logi')
     else:
        form=SignupForm()
     return render(request,'register.html',{'form':form})

def login(request):
    if request.method == "POST":
        em=request.POST['txtemail']
        pwd=request.POST['txtpassword']
        try:
            d1=Register.objects.get(email=em,password=pwd)
        except Register.DoesNotExist:
            return redirect('logi')
        else:  
            request.session['uid'] = d1.id
            return redirect("pro")
    else:
        return render(request,'login.html')

def profile(request):
    if(request.session.get('uid')):
        uid=request.session['uid']
        d1=Register.objects.get(id=uid)
        return render(request,'dashboard.html',{'uid':d1})
    else:
        return render(request,'login.html')

def logout(request):
        del request.session['uid']    
        return redirect('logi')

def resetpwd(request,id):
    if request.method == 'POST':
        otp=request.POST['txtotp']
        pwd=request.POST['txtpassword1']
        pwd1=request.POST['txtpassword2']
        if not Otp.objects.filter(otp=otp).first():
            messages.success(request,'OTP is not valid. please enter valid OTP')
            return redirect('reset')
        user_obj=Register.objects.get(pk=id)
        print(user_obj)
        user_obj.password= pwd
        user_obj.save()
        return redirect('logi')
    return render(request,'resetpwd.html')

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(6) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
    data=''
    if request.method == 'POST':
        email=request.POST['txtemail']
        data=Register.objects.filter(email=email).first()
        print(data.id)
        if not Register.objects.filter(email=email).first():
            messages.success(request,'Not email found with this email')
            return redirect('sdo')       
        o=generateOTP()
        otp = Otp.objects.create(email=email,otp=o)
        otp.save()
        htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
        send_mail('OTP request',o,'email',[email],fail_silently=False,html_message=htmlgen)
    return render(request,'sendotp.html',{'data':data})


