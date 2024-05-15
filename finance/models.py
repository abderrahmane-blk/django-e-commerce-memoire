from django.db import models
from store.models import Cart
from django.contrib.auth.models import User
from accounts.models import Vendor_info
from store.models import Store
# Create your models here.

"""a transaction is made when a user tries to buy (products checked then total counted)
if payment is success , orders are sent to vendors
(in case declined (with execuse) product price payed back to customer) if vendors send product 
vendors are payed"""
class transactionStatus(models.TextChoices):
    PENDING ='pending', 'Pending Approval'
    COMPLETED ='completed', 'transaction completed'
    CANCELED='CANCELED', 'transaction canceled'
    

class Transaction(models.Model):
    cart=models.ForeignKey(Cart,null=True, on_delete=models.SET_NULL)
    total = models.DecimalField( max_digits=10, decimal_places=2 )
    customer = models.OneToOneField(User ,null=True ,on_delete=models.SET_NULL) #null because the customer could be anonymous

    created_at =models.DateTimeField(auto_now_add=True)

    status =models.CharField(max_length=50 ,choices=transactionStatus.choices ,default =transactionStatus.PENDING)






class Order(models.Model):
    price_paid = models.DecimalField(max_digits=6, decimal_places=2 ,null=False)# the price indicates how much it is when the customer clicks buy
    quantity =models.IntegerField(default=1)

    customer = models.OneToOneField(User ,on_delete=models.SET_NULL, null=True) #may be it has to be changed to PROTECT , but that will do problems deleting the users from the database
    store = models.ForeignKey(Store ,on_delete=models.SET_NULL, null=True)

    the_transaction = models.ForeignKey(Transaction ,on_delete=models.SET_NULL, null=True)



    created_on = models.DateTimeField(auto_now_add=True)
























