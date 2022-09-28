from django.contrib import admin
from .models import Service,Skill,Message,Project
# Register your models here.
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Message)
