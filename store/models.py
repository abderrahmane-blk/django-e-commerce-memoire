from django.db import models
from accounts.models import Vendor_info ,Customer_info,User
from django.contrib.sessions.models import Session

#from django.core.validators import MinValueValidator,MaxValueValidator





class Category(models.Model):
    name = models.CharField(max_length=255 ,unique=True)

    def __str__(self) -> str:
        return self.name



class Store(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)

    store_name = models.CharField( max_length=512 ,null=True)
    location = models.CharField(max_length=5000,null=True)
    slogan = models.CharField(max_length=2048 , null =True)
    logo = models.ImageField( blank=True, null=True ,upload_to='stores_images')
    deposit_account = models.CharField(max_length = 100 ,default='0000 0000 0000 0000')

    def __str__(self) -> str:
        return self.store_name



class Product(models.Model):
    name = models.CharField(max_length=255)
    small_description=models.CharField(max_length=1500,null=True)
    #slug = models.SlugField(unique=True, blank=True)  # Auto-generate slug from title
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Consider using DecimalField for currency
    promotion_price= models.DecimalField(max_digits=8, decimal_places=2 ,null=True )  # Consider using DecimalField for currency
    #condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    image = models.ImageField( blank=True, null=True)  # Define image upload path
    featured = models.BooleanField(default=False)
    quantity = models.IntegerField(default = 10)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    store = models.ForeignKey(Store ,on_delete=models.CASCADE   ,null=True)#delete the null later


    category = models.ForeignKey(Category,on_delete = models.SET_NULL ,null=True) #or we do PROTECT :so it would be interdicted to delete a category that has products



    def __str__(self) -> str:
        return self.name
    
    def get_discount(self) -> int:
        res= 100 - self.promotion_price *100 /self.price
        return (res*10 //1)/10 #to keep only 2 decimals after the point
    
    def is_discounted(self):
        if self.promotion_price == None or self.promotion_price == self.price :return False
        else :return True






# about the cart

class Cart(models.Model):
    items = models.JSONField(default=dict)
    session = models.ForeignKey(Session,  on_delete=models.CASCADE)

class Cart_item(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1,null=False ,)#add a validator here





# about the comparer

class Comparer(models.Model):
    session = models.ForeignKey(Session,  on_delete=models.CASCADE)

class Comparer_product(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    comparer = models.ForeignKey(Comparer , on_delete=models.CASCADE)







class Order(models.Model):
    total = models.DecimalField(max_digits=6, decimal_places=2)
    
    created_on = models.DateTimeField(auto_now_add=True)

    customer = models.ForeignKey(User ,on_delete=models.SET_NULL, null=True) #may be it has to be changed to PROTECT , but that will do problems deleting the users from the database

    def __str__(self) -> str:
        return self.id














