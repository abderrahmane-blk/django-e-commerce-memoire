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



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'total' ,'created_on','customer']
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id', 'items' ,'session']
