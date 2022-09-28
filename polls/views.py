from django.shortcuts import render,HttpResponse,redirect
from .models import Service,Skill,Project
# Create your views here.

def home(request):
    allpost = Service.objects.all()
    skills = Skill.objects.all()
    project = Project.objects.all()
    return render(request,'polls/home.html',{'allpost':allpost,'skills':skills,'project':project})


# def skill(request):
#     skills = Skill.objects.all()
#     return render(request,'polls/home.html',{'skills':skills})