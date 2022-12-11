from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url='signup')
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                return render(request,'signup.html')
            else:
                user=User.objects.create(username=username,password=password)
                user.save()
                return render(request,'login.html')
        else:
            return render(request,'signup.html')
    
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
          return redirect('home')
    return render(request,'login.html')
@login_required(login_url='signup')
def logout(request):
    auth.logout(request)
    return redirect('signup')