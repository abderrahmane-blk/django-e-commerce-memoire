from django import forms



attributes ={#'type':'password',
            
            }

class New_vendor_form(forms.Form):
    #userproperties first
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255 ,required=True)
    email = forms.EmailField(required=True)

    password1 = forms.CharField(max_length =255 ,required =True ,widget=forms.TextInput(attrs={'type':'password' , 'label':'Password'}))
    password2 = forms.CharField(max_length =255 ,required =True ,widget=forms.TextInput(attrs={'type':'password','label':'Confirm Password'}))

    #Vendor properties
    vendor_specific_property = forms.CharField(max_length=255)

    store_deposit_account = forms.CharField(max_length = 32 ,required=True )



