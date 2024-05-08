from django import forms



attributes ={#'type':'password',
            
            }

register_attrs ={'class':'form-control form-control-lg bg-light fs-6 '}


class New_vendor_form(forms.Form):
    #userproperties first
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs=register_attrs))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs=register_attrs))
    username = forms.CharField(max_length=255 ,required=True, widget=forms.TextInput(attrs=register_attrs))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs=register_attrs))

    password1 = forms.CharField(max_length =255 ,required =True ,widget=forms.TextInput(attrs={'type':'password' , 'label':'Password','class':'form-control form-control-lg bg-light fs-6'}))
    password2 = forms.CharField(max_length =255 ,required =True ,widget=forms.TextInput(attrs={'type':'password','label':'Confirm Password','class':'form-control form-control-lg bg-light fs-6'}))

    # customer properties
    lives_in = forms.CharField(max_length=1000 ,required=False, widget=forms.TextInput(attrs=register_attrs))

    #Vendor properties
    bio = forms.CharField(max_length=2024  ,required=False, widget=forms.Textarea(attrs=register_attrs))
    
    #store properties
    # store_name = forms.CharField(max_length=255 ,required=True, widget=forms.TextInput(attrs=register_attrs))
    deposit_account =forms.CharField(max_length=255 ,required=True, widget=forms.TextInput(attrs=register_attrs))



class New_customer_form(forms.Form):
    #userproperties first
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs=register_attrs))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs=register_attrs))
    username = forms.CharField(max_length=255 ,required=True, widget=forms.TextInput(attrs=register_attrs))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs=register_attrs))

    password1 = forms.CharField(max_length =255 ,required =True ,widget=forms.TextInput(attrs={'type':'password' , 'label':'Password','class':'form-control form-control-lg bg-light fs-6'}))
    password2 = forms.CharField(max_length =255 ,required =True ,widget=forms.TextInput(attrs={'type':'password','label':'Confirm Password','class':'form-control form-control-lg bg-light fs-6'}))

    # customer properties









# down here is useless


login_form_email_attrs ={'':''}
login_form_password_attrs ={'':''}

class login_form(forms.Form):
    email = forms.EmailField( required=True ,widget=forms.TextInput(attrs=login_form_email_attrs))
    password = forms.EmailField(required=True ,widget=forms.PasswordInput(attrs=login_form_password_attrs)) 