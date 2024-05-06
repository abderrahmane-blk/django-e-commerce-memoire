from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.hashers import make_password
# Create your views here.






def test_if_logged_in(request):
    return render(request , 'test.html')



#Customers 



#Vendors
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


            #for vendor_info model
            vendor_specific_property=form.cleaned_data['vendor_specific_property']
            store_deposit_account =form.cleaned_data['store_deposit_account']
            
            Vendor_info.objects.create(vendor_specific_property=vendor_specific_property , store_deposit_account=store_deposit_account ,user=new_user)

            
            print(new_user)
            print('-------worked----------')

        print('-------not registers , redirect to login----------')
        return redirect('login')
        pass

    form =New_vendor_form()
    return render(request,'registration/register_vendor.html' ,{'form':form})





def register_customer(request):


    return render(request ,'registration/register_customer_test.html')














