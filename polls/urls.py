from django.contrib import admin
from django.urls import path
from polls import views         

urlpatterns = [
    path('',views.home,name='home'),
    path('polls/message',views.message,name='message'),
]
