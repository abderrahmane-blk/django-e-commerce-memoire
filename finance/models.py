from django.db import models
from store.models import Cart
from django.contrib.auth.models import User
from accounts.models import Vendor_info
from store.models import Store,Product
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
    customer = models.ForeignKey(User ,null=True ,on_delete=models.SET_NULL) #null because the customer could be anonymous
    more_info=models.JSONField(blank=True, null=True)
    payment_method =models.CharField(max_length=50 ,null=True)

    created_at =models.DateTimeField(auto_now_add=True)

    status =models.CharField(max_length=50 ,choices=transactionStatus.choices ,default =transactionStatus.PENDING)



class OrderStatus(models.TextChoices):
    TO_BE_SENT ='to be sent', ' to be sent'
    SENT ='sent', 'order sent'
    CANCELED='CANCELED', 'order canceled'
    

class Order(models.Model):
    item =models.OneToOneField(Product, on_delete=models.SET_NULL ,null=True)
    price_paid = models.DecimalField(max_digits=6, decimal_places=2 ,null=False)# the price indicates how much it is when the customer clicks buy
    quantity =models.IntegerField(default=1)

    customer = models.ForeignKey(User ,on_delete=models.SET_NULL, null=True) #may be it has to be changed to PROTECT , but that will do problems deleting the users from the database
    store = models.ForeignKey(Store ,on_delete=models.SET_NULL, null=True)

    the_transaction = models.ForeignKey(Transaction ,on_delete=models.SET_NULL, null=True)

    order_status =models.CharField(max_length=50 ,choices=OrderStatus.choices ,default =OrderStatus.TO_BE_SENT)

    created_on = models.DateTimeField(auto_now_add=True)






# not in DB


from chargily_epay_django.models import AnonymPayment ,FakePaymentMixin
from django.conf import settings


class ChargilyPayment(FakePaymentMixin,AnonymPayment):
    webhook_url = 'payment-confirmation' # reverse url
    back_url = 'payment-status'
    fake_payment_url = "fake-payment" # reverse url




















