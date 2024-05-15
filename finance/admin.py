from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'price_paid' ,'quantity' ,'created_on','customer']