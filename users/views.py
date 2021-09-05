from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            db_entry=User.objects.create_user(username=username,email=email,password=password)
            db_entry.save()
            return render(request,'users/login.html')
    return render(request,'users/login.html')
