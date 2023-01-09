from re import sub
from django.shortcuts import render,HttpResponse,redirect
from .models import Service,Skill,Project,Message
from django.core.mail import send_mail

# Create your views here.

def home(request):
    allpost = Service.objects.all()
    skills = Skill.objects.all()
    project = Project.objects.all()
    counting = Project.objects.count
    return render(request,'polls/home.html',{'allpost':allpost,'skills':skills,'project':project,'count':counting})

def message(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        send  = Message(name = name , email = email , subject = subject , message = message)
        send.save()
        send_mail(subject,message + ' from ' + email,'devopsgarg@gmail.com',['himanshubansal9818812568@gmail.com'],fail_silently=False,)
        allpost = Service.objects.all()
        skills = Skill.objects.all()
        project = Project.objects.count()
        print('hii')
        return render(request,'polls/home.html',{'allpost':allpost,'skills':skills,'project':project})
        


# def skill(request):
#     skills = Skill.objects.all()
#     return render(request,'polls/home.html',{'skills':skills})