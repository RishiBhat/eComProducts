from django.shortcuts import render, HttpResponse, redirect
#from main.models import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'base.html')

@login_required(login_url="index")
def home(request):
    obj = Product.objects.all()
    for i in obj:
        print(obj)
        print(i.id)
        print(i.prname)
    # profile = {"id" : obj.id}
    return render(request, 'home.html', {'profile':obj})
    # return render(request,'home.html')


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")



def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
   

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your ProjectTask has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")




def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')



   # profile = {"id" : obj.id, "name" : obj.email, "pr, "city" : obj.city}
   # return render(request, 'home.html', {'profile':profile})

####################################################################################



#we will form the table of prouct here in views


from .models import Product

def prod(request, id):
    params = Product.objects.get(id=id)
    print(params)
    print(params.id)
    print(params.prname)
    #profile = {"id" : obj.id, "name" : obj.name, "email" : obj.email, "password" : obj.password, "desc" : obj.desc}
    return render(request, 'prod.html', {'params':params})



