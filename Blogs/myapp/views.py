from django.shortcuts import render
from myapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# def show(request):
	#return render(request, 'base.html')

def Ayush(request):
	return render(request,'result.html')

def django(request):
	return render(request,'Django.html')

def djangorest(request):
	return render(request,'DjangoRs.html')

def cont(request):
    if request.method=="POST":
      firstname= request.POST.get('firstname')
      lastname= request.POST.get('lastname')
      Address= request.POST.get('Address')
      
      subject= request.POST.get('subject')

      contact_s=Contact(firstname=firstname,lastname=lastname,Address=Address,subject=subject)
      contact_s.save()
      messages.success(request, 'Profile details updated.')
      print("You are succefully added")
  
  
    
  
  
    return render(request,'contact.html')


def Inv(request):
	return render(request,'interview.html')
 


def Sign(request):
    
    return render(request, "signup.html")

def log(request):
   
            
    return render(request, "login.html")






