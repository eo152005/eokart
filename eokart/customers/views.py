from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer

# Create your views here.

def show_account(request):

  if request.POST and 'signup_button' in request.POST:
    try:    

        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone_number=request.POST.get('phone_number')

        #creates user account
        user=User.objects.create(
            username=username,
            password=password,
            email=email
        )
        #customer account
        customer=Customer.objects.create(
            user=username,
            address=address,
            phone=phone_number
        )
        return redirect('home') 
    except Exception as e:
          error_message="Username Already Taken!"
          messages.error(request,error_message)


  return render(request,'account.html')