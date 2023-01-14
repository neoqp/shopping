from django.shortcuts import *
from django.contrib import auth
from django.contrib.auth import *
from django.contrib.auth.models import *

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],                      
            )
            auth.login(request,user)
            return redirect('/')
        return render(request,'signup.html')
    return render(request,'signup.html')