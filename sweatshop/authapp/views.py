from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def Home(request):
    return render(request, "index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"user is Created Please Login")
        return redirect('/login')
    return render(request, "signup.html")

def handlelogin(request):
    return render(request, "login.html")