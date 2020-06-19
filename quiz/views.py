from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Exam

# Create your views here.
def home(request):
    if request.method == 'POST':
        Ques = request.POST.get('Question')
        Op1 =  request.POST.get('Option1')
        Op2 =  request.POST.get('Option2')
        Op3 =  request.POST.get('Option3')
        Op4 =  request.POST.get('Option4')
        Cans =  request.POST.get('Corrans')
        s = Exam(Question=Ques,Option1=Op1,Option2=Op2,Option3=Op3,Option4=Op4,Corrans=Cans)
        s.save()
    return render(request,"quiz.html",{})