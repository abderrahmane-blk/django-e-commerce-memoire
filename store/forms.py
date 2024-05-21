from django import forms



class CategoryNameForm(forms.Form):
    new_name = forms.CharField(max_length=255)
    









