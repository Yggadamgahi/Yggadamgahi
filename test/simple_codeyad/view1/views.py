from django.shortcuts import render , HttpResponse
from .models import Class

def course_list(req):
            course = Class.objects.all()
            return render(req,'v1temps/temp2.html',context={'context':course})

def view1(req):
    return render(req,'v1temps/temp1.html')
    


