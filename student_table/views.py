from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.core.mail import send_mail
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate, login, logout


# @login_required
def loginhandle(request):
    if(request.method=='POST'):
        username=request.POST['uname']
        password=request.POST['pass']
        user=authenticate(username=username, password=password)
        if(user is not None):
            if(user.is_active):
                login(request,user)
                messages.success(request,"Successfully logged in")
                return render(request,"loginhandle.html")
			
        else:
            messages.error(request,"User is not registered")
    return render(request,"loginhandle.html")

            
def logouthandle(request):
	logout(request)
	messages.success(request,"Successfully logged out")
	return redirect('/')

def home(request):
    return render(request,"home.html")
    


def register(request):
    if(request.method=='POST'):
        ref_code = request.POST['ref_code']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username= request.POST['username']
        parent_name = request.POST['parent_name']
        dob = request.POST['dob']
        country =request.POST['country']
        address = request.POST['address']
        school=request.POST['school']
        school_state = request.POST['school_state']
        school_address=request.POST['school_address']
        school_city=request.POST['school_city']
        pincode = request.POST['pincode']
        number=request.POST['number']
        email = request.POST['email']
        password =request.POST['password']
        standard = request.POST['standard']

        enc_password = pbkdf2_sha256.encrypt(password, rounds=8000, salt_size=10)
        if(Student.objects.filter(email=email).exists()):
            messages.warning(request,"Email already exists")
        else:
            if(Student.objects.filter(username=username).exists()):
                messages.warning(request,"Username already exists")
            else:
                context=Student(ref_code = ref_code ,first_name=first_name,username=username, last_name=last_name,parent_name = parent_name,dob = dob,country= country,address= address,school=school,school_state= school_state,school_address= school_address,school_city= school_city,pincode=pincode,number=number,email=email,standard= standard,password= password)
                context.save()
                messages.success(request,"Student Registered successfully")
            # user.is_active=False
            # user.save()




    return render(request,'register.html')


# Create your views here.
