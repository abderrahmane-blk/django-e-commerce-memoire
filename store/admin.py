from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'name' ,'small_description','price', 'category','image','featured','quantity','owner']
    list_editable=['name' ,'featured' ,'category']



@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display=['id', 'store_name' ,'location' ,'deposit_account']


    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id', 'items' ,'session']
