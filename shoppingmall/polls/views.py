from django.shortcuts import render
from django.http import *

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def create(request):
    return render(request, 'polls/create.html')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    
    elif request.method=='POST':
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)

    res_data={}

    if not (username and password):
        res_data['error']="input all values"