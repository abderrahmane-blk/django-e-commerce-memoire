from django.db import models
from accounts.models import Vendor_info ,Customer_info,User
from django.contrib.sessions.models import Session

#from django.core.validators import MinValueValidator,MaxValueValidator





class Category(models.Model):
    name = models.CharField(max_length=255 ,unique=True)

    def __str__(self) -> str:
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=255)
    small_description=models.CharField(max_length=1500,null=True)
    #slug = models.SlugField(unique=True, blank=True)  # Auto-generate slug from title
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Consider using DecimalField for currency
    #promotion= models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(99)] ,null=True)
    promotion_price= models.DecimalField(max_digits=8, decimal_places=2 ,null=True )  # Consider using DecimalField for currency
    #condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    image = models.ImageField( blank=True, null=True)  # Define image upload path
    featured = models.BooleanField(default=False)
    quantity = models.IntegerField(default = 10)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(Vendor_info, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.SET_NULL ,null=True) #or we do PROTECT :so it would be interdicted to delete a category that has products



    def __str__(self) -> str:
        return self.name
    
    def get_discount(self) -> int:
        res= 100 - self.promotion_price *100 /self.price
        return (res*10 //1)/10 #to keep only 2 decimals after the point
    
    def is_discounted(self):
        if self.promotion_price == None :return False
        if self.promotion_price == self.price :return False
        else :return True




class Order(models.Model):
    total = models.DecimalField(max_digits=6, decimal_places=2)
    
    created_on = models.DateTimeField(auto_now_add=True)

    customer = models.ForeignKey(User ,on_delete=models.SET_NULL, null=True) #may be it has to be changed to PROTECT , but that will do problems deleting the users from the database

    def __str__(self) -> str:
        return self.id





class Cart(models.Model):
    items = models.JSONField(default=dict)
    session = models.ForeignKey(Session,  on_delete=models.CASCADE)

class Cart_item(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1,null=False ,)#add a validator here


















