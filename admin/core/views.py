from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')    

def signuppage(request):
    if request.method=="POST":
        fname = request.POST['first_name'] 
        lname = request.POST['last_name']
        unm = request.POST['username']    
        email = request.POST['email']
        pwd = request.POST['password']
    try:
       user=User.objects.get(username=unm)
       return render(request,'signup.html')
    except:
        user=User.objects.create_user(first_name=fname,last_name=lname,username=unm,email=email,password=pwd)
        user.save()
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')



def signinpage(request):
    if request.method=="POST":
      unm = request.POST['username']
      pwd = request.POST['password']
      user=auth.authenticate(username=unm ,password=pwd)
      if user is not None:
          auth.login(request,user)
          return redirect('signup')
      else:
        return render(request,'signin.html')
    else:
        return render(request,'signin.html')
   
       
