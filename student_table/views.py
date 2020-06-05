from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.core.mail import send_mail
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate, login, logout



from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView

from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from student_table.tokens import account_activation_token

def loginhandle(request):
    if(request.method=='POST'):
        username=request.POST['email']
        password=request.POST['pass']
        user=authenticate(email=username, password=password)
        if(user):
            if(user.is_active and user.email_confirmed):
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

        if(Student.objects.filter(email=email).exists()):
            messages.warning(request,"Email already exists")
        else:
            if(Student.objects.filter(username=username).exists()):
                messages.warning(request,"Username already exists")
            else:
                context=Student(ref_code = ref_code ,first_name=first_name,username=username, last_name=last_name,parent_name = parent_name,dob = dob,country= country,address= address,school=school,school_state= school_state,school_address= school_address,school_city= school_city,pincode=pincode,number=number,email=email,standard= standard)
                context.set_password(password)
                context.save()

                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('account_activation_email.html', {
                'user': context,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(context.pk)),
                'token': account_activation_token.make_token(context),
                })
                send_mail(subject, message,'bhatchandan99@gmail.com',['chandan.me17@iitp.ac.in','bhatchandan99@gmail.com',],fail_silently=False,)


                messages.success(request, ('Please Confirm your email to complete registration.'))
                return render(request,"loginhandle.html")

            # user.is_active=False
            # user.save()




    return render(request,'register.html')

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from student_table.tokens import account_activation_token

class ActivateAccount(View):


    def get(self, request, uidb64, token, *args, **kwargs):
            try:
                uid = force_text(urlsafe_base64_decode(uidb64))
                user = Student.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, Student.DoesNotExist):
                user = None

            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.email_confirmed = True
                user.save()
                login(request, user)
                messages.success(request, ('Your account have been confirmed.'))
                return redirect('/')
            else:
                messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
                return redirect('/')


# Create your views here.
