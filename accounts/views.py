from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth.models import User
from store.models import Store
from .forms import *
from django.contrib.auth.hashers import make_password


import time

def timer(fn):
    def wrapper(*args,**kwargs):
        start = time.time()
        res =fn(*args ,**kwargs)
        end =time.time() - start
        print('---------')
        print('total:',end)
        print('---------')

        return res
    return wrapper




# Create your views here.





@timer
def test_if_logged_in(request):
    return render(request , 'test.html')



#Customers 



#Vendors
@timer
def register_vendor(request):
    if request.method == 'POST':
        form = New_vendor_form(request.POST)
        if form.is_valid():
            #for user model
            username =form.cleaned_data['username']
            first_name =form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            password1=form.cleaned_data['password1']
            password2 =form.cleaned_data['password2']
            email =form.cleaned_data['email']

            if password1 and password2 and password1 !=password2:
                form2 = New_vendor_form(request.POST)
                return render(request , 'registration/register_vendor.html' ,{'form':form2 ,'error' :'passwords did not match'})
            if User.objects.filter(username=username):
                form2 = New_vendor_form(request.POST)
                return render(request , 'registration/register_vendor.html' ,{'form':form2 ,'error' :'this username is already taken'})
            
            if User.objects.filter(email=email):
                form2 = New_vendor_form(request.POST)
                return render(request , 'registration/register_vendor.html' ,{'form':form2 ,'error' :'this email is already registerd for another user'})
            

            new_user=User.objects.create(username=username , password=make_password(password1) ,email=email,first_name=first_name ,last_name=last_name )

            #for customer_info model
            try:
                lives_in=form.cleaned_data['lives_in']
            except:
                lives_in =None
            new_customer_info=Customer_info.objects.create(lives_in=lives_in, user=new_user)
            # new_customer_info.save()
            
            print(new_customer_info)
            """
            change it to save later
            """


            #for vendor_info model
            new_bio=form.cleaned_data['bio']
            new_vendor_info=Vendor_info.objects.create(bio =new_bio, user=new_user)
            # new_vendor_info.save()
            
            print(new_vendor_info)
            """
            change it to save later
            """



            # the store of the vendor
            store_name = form.cleaned_data['bio']
            deposit_account = form.cleaned_data['bio']

            new_store =Store.objects.create(store_name=store_name ,deposit_account =deposit_account ,user =new_user)
            # new_store.save()
            print(new_store)
            """
            change it to save later
            """




            
            print(new_user)
            print('-------worked----------')

        print('-------not registered , redirect to login----------')
        return redirect('login')


    form =New_vendor_form()
    return render(request,'registration/register_vendor.html' ,{'form':form})




@timer
def register_customer(request):
    print(request.method)
    if request.method == 'POST':
        form = New_customer_form(request.POST)
        if form.is_valid():
            #for user model
            username =form.cleaned_data['username']
            first_name =form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            password1=form.cleaned_data['password1']
            password2 =form.cleaned_data['password2']
            email =form.cleaned_data['email']

            if password1 and password2 and password1 !=password2:
                form2 = New_customer_form(request.POST)
                return render(request , 'registration/signup.html' ,{'form':form2 ,'error' :'passwords did not match'})
            if User.objects.filter(username=username):
                form2 = New_customer_form(request.POST)
                return render(request , 'registration/signup.html' ,{'form':form2 ,'error' :'this username is already taken'})
            
            if User.objects.filter(email=email):
                form2 = New_customer_form(request.POST)
                return render(request , 'registration/signup.html' ,{'form':form2 ,'error' :'this email is already registerd for another user'})
            

            new_user=User.objects.create(username=username , password=make_password(password1) ,email=email,first_name=first_name ,last_name=last_name )
            new_user.save()
       
            
            print(new_user.username)
            print('-------worked----------')


        return redirect('login')
    
    form = New_customer_form()

    return render(request ,'registration/signup.html' ,{'form':form})














