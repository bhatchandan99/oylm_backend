from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from passlib.hash import pbkdf2_sha256



class Student(AbstractUser):
    id=models.AutoField(primary_key=True)
    ref_code = models.CharField(default="000",max_length=20)
    parent_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    country = CountryField()
    address = models.CharField(null=False,max_length=100,default="lane")
    school=models.CharField(max_length=100,null=False,default="abc")
    school_state = models.CharField(max_length=100,null=False,default="abc")
    school_address=models.CharField(max_length=100,null=False,default="abc")
    school_city=models.CharField(max_length=100,null=False,default="abc")
    pincode = models.IntegerField(null=False, default=0)
    number = models.IntegerField(null=False, default=0)
    standard = models.CharField(null=False, max_length=10,default=1)
    email = models.CharField(max_length=150, null=False,unique=True)
    email_confirmed = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)



class Olympiad(models.Model):
    id=models.AutoField(primary_key=True)
    student = models.ForeignKey("Student", on_delete=models.CASCADE, default=1)
    mathsolym=models.BooleanField(default=False)
    scienceolym=models.BooleanField(default=False)
    englisholym=models.BooleanField(default=False)
    reasoningolym=models.BooleanField(default=False)
    cyberolym=models.BooleanField(default=False)
    internationalspell=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    



    
