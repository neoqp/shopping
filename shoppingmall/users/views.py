from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['confirm']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request,user)
            return redirect('/')
        
    else:
        return render(request, 'users/signup.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        
        else:
            return render(request, 'users/login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request,'users/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('/')
    
    else:
        return render(request,'users/login.html')