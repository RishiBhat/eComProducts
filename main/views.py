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



#we will form the table of prouct here in views with the use of forms and admin and the models 

from .forms import ProductForm
from .models import Product





def form(request):
    
        form = ProductForm()
        if request.POST:
            form= ProductForm(data= request.POST, files=request.FILES)
            if form.is_valid:
                form.request.get('prtotal')
                form.request.get('prprice')
                form.request.get('prqty')
                prtotal=request.POST['prprice'*'prqty'] 
                form.save()
                return redirect('home')

        return render(request,'prform.html', {'form': form})


#Here the product display is done which I will be using it for the later


def prod(request):
    params = Product.objects.all()
    print(params)
    return render(request, 'prod.html', {'params':params})


def update(request,id):
    ris = Product.objects.get(id=id)
    form=ProductForm(instance=ris, data=request.POST or None, files=request.FILES or None) 
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'prform.html',{'form':form})
    
    
    
    
def delete(request, id):
    bt= Product.objects.get(id=id)
    bt.delete()
    return redirect('home')



#here we will create a single product list 


def prolist(request,id):
   
     ris = Product.objects.get(id=id)
     
     print(ris.prprice)
     return HttpResponse("working")
