from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Customer_info)
class Customer_infoAdmin(admin.ModelAdmin):
    list_display=['id','lives_in']



@admin.register(Vendor_info)
class Vendor_infoAdmin(admin.ModelAdmin):
    list_display=['id','user','bio',  ]



















