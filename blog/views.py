from django.shortcuts import render,HttpResponse
# Create your views here.
def blogpost(request):
    return HttpResponse('Blog post')