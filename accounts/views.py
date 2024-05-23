from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth.models import User
from store.models import Store
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserTypes
from django.contrib.auth import update_session_auth_hash


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password



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


def is_permitted(request):
    try:
        if request.user.is_banned:
            print('banned')
    except:
        print('no user')





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
            

            new_user=User.objects.create(username=username ,usertype='customer', password=make_password(password1) ,email=email,first_name=first_name ,last_name=last_name )

            #for customer_info model
            try:
                lives_in=form.cleaned_data['lives_in']
                new_customer_info=Customer_info.objects.create(lives_in=lives_in, user=new_user)

            except:
                lives_in =None
                new_customer_info=Customer_info.objects.create(user=new_user)
            new_customer_info.save()
            
            print(new_customer_info)
            """ 
            change it to save later   
            """


            #for vendor_info model
            new_bio=form.cleaned_data['bio']
            new_vendor_info=Vendor_info.objects.create(bio =new_bio, user=new_user)
            new_vendor_info.save()
            
            print(new_vendor_info)
            """
            change it to save later  ^ fix it
            """



            # the store of the vendor
            store_name = form.cleaned_data['store_name']
            deposit_account = form.cleaned_data['deposit_account']

            new_store =Store.objects.create(store_name=store_name ,deposit_account =deposit_account ,vendor =new_user)
            new_store.save()
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
            

            new_user=User.objects.create(username=username , password=make_password(password1) ,email=email,first_name=first_name ,last_name=last_name ,usertype='customer')
            new_user.save()
            # New_customer_info =
            Customer_info.objects.create(user=new_user).save()
       
            
            print(new_user.username)
            print('-------worked----------')


        return redirect('login')
    
    form = New_customer_form()

    return render(request ,'registration/signup.html' ,{'form':form})



@csrf_exempt
def profile(request):

    if request.method=='POST':
        errors_in_form=[]

        form =request.POST

        self_pic =None
        try:
            self_pic =request.FILES['the_personal_pic']
        except:
            pass

        the_username=form['the_username']
        the_firstname=form['the_first_name']
        the_lastname=form['the_lastname']
        the_email=form['the_email']

        current_password=form['current_password']
        new_password=form['new_password']
        new_password_confirmation=form['new_password_confirmation']

        where_lives=form['where_lives']



        # updating the user object
        the_user=User.objects.get(pk=request.user.id)
        print(the_user)

        if the_username and the_username !=''  :
            if User.objects.filter(username=the_username).first() is None:
                the_user.username=the_username
            else:
                errors_in_form.append('another user alrready have this username')

        if the_firstname !='':
            the_user.first_name=the_firstname
        if the_lastname !='':
            the_user.last_name =the_lastname

        if the_email and User.objects.filter(email=the_email).first() is None:
            email_Form =emailForm(data={'mail': the_email})
            if email_Form.is_valid():
                the_user.email =email_Form.cleaned_data['mail']
                update_session_auth_hash(request, the_user)

        # the password section
        print('------------')
        print('password section')
        print('------------')

        if check_password(current_password,the_user.password):
            print('-----1-------')
            if new_password and new_password_confirmation and new_password_confirmation !='' and new_password !='' and new_password ==new_password_confirmation:
                the_user.password =make_password(new_password)
                the_user.save()

                update_session_auth_hash(request, the_user)  # Important! so the user wont be logged out

                print('the new password is :',new_password )

            else :
                print('something went wrong')
        else:
            print('passwords did not match')
        
        
        the_user.save()


        # the customer info section
        customer_info =Customer_info.objects.filter(user=the_user).first()

        if where_lives != '' and where_lives != customer_info.lives_in:
            customer_info.lives_in =where_lives

        if self_pic :
            customer_info.image =self_pic
        
        customer_info.save()
        
        # the vendor info section
        if request.user.usertype != 'customer':
            vendor_info =Vendor_info.objects.filter(user=the_user).first()
            
            the_bio=form['the_bio']

            # updating the vendor_info
            if the_bio and the_bio !='' and the_bio !=vendor_info.bio:
                vendor_info.bio =the_bio
                vendor_info.save()

            #the sore info 

            the_store_logo =None
            try:
                the_store_logo =request.FILES['the_store_logo']
            except:
                pass

            the_store_name=form['the_store_name']
            the_slogan=form['the_slogan']
            the_location=form['the_location']
            the_store_deposit_account=form['the_store_deposit_account']

            the_store =Store.objects.filter(vendor=the_user).first()

            if the_store_name and the_store_name.strip() !='' and the_store_name !=the_store.store_name :
                the_store.store_name =the_store_name

            if the_slogan and the_slogan.strip() !='' and the_slogan !=the_store.slogan :
                the_store.slogan =the_slogan
            
            if the_location and the_location.strip() !='' and the_location !=the_store.location :
                the_store.location =the_location
            
            if the_store_deposit_account and the_store_deposit_account.strip() !='' and the_store_deposit_account !=the_store.deposit_account :
                the_store.deposit_account =the_store_deposit_account
            
            if the_store_logo :
                the_store.logo =the_store_logo

            the_store.save()
            print('--------------store')




        #we login


    user =request.user
    if user.usertype =='customer':
        the_user=User.objects.filter(pk=user.id).first()
        the_customer_info =Customer_info.objects.filter(user=request.user).first()

        return render(request,"profile.html" ,{'the_user':the_user ,'the_customer_info':the_customer_info})


    else:
        the_user=User.objects.filter(pk=user.id).select_related('vendor_info').select_related('customer_info').first()
        the_customer_info =Customer_info.objects.filter(user=request.user).first()
        the_vendor_info =Vendor_info.objects.filter(user=request.user).first()
        the_store =Store.objects.filter(vendor=the_user).first()

        return render(request,"profile.html" ,{'the_user':the_user 
                                               ,'the_vendor_info':the_vendor_info 
                                               ,'the_customer_info':the_customer_info 
                                               ,'the_store':the_store})





    









