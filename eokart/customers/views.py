from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer

# Create your views here.

def show_account(request):
  
  context={}
  if request.POST and 'signup_button' in request.POST:
    context['signup_button']=True
      
    try:
         username=request.POST.get('username')
         password=request.POST.get('password')
         email=request.POST.get('email')
         address=request.POST.get('address')
         phone_number=request.POST.get('phonenumber')


        # Create the User object
         user=User.objects.create_user(
             username=username,
             email=email,
             password=password
    )

        # Create the associated Customer object
         customer=Customer.objects.create(
            user=user,
            address=address,
            phone=phone_number
    )
         sucess_message="User Registered Successfully"
         messages.success(request,sucess_message)
        
    except Exception as e:
       error_message="Username Already Taken"
       messages.error(request,error_message)

  if request.POST and 'login' in request.POST:
      context['signup_button']=False
     
      username=request.POST.get('username')
      password=request.POST.get('password')
     
      user=authenticate(username=username,password=password)
      if user: 
         login(request,user)
         return redirect('home')
      else:
         messages.error(request,'Invalid User')
         
   
  return render(request,'account.html',context)


def sign_out(request):
   logout(request)
   return redirect('home')


