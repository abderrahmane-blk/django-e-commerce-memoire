from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'price_paid' ,'quantity' ,'created_on','customer']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=[
    'total','customer','more_info','payment_method','created_at','status']