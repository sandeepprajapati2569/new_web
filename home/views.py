from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request,'home.html')

def message(request):
        name=request.GET['first-name']
        sname=request.GET['last-name']
        email=request.GET['email']
        number=request.GET['phone']
        message=request.GET['message']

        user=User.objects.create_user(first_name=name,last_name=sname,email=email,number=number,message=message)
        user.save()
        return redirect('/')
