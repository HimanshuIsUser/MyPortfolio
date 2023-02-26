from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models

# Create your models here.
class Service(models.Model):
    sno = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='polls/images',default="")
    role = models.TextField()
    resume = models.FileField(upload_to='polls/files',default="")

    def __str__(self):
        return f'{self.sno} : {self.role}'

class Skill(models.Model):
    sno = models.AutoField(primary_key=True)
    name=models.CharField(max_length=111)
    width=models.CharField(max_length=111)

    def __str__(self):
        return f'{self.sno} : {self.name}'

class Project(models.Model):
    sno = models.AutoField(primary_key=True)
    pic = models.ImageField(upload_to='polls/images',default="")
    name = models.CharField(max_length=111)
    domain = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.sno} : {self.name}'


class Message(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return f'{self.sno} : {self.email}'

