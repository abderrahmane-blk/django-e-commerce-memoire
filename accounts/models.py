from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_TYPE_CHOICES = (
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
    )


class Vendor_info(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)

    store = models.CharField(max_length = 255 ,null=True ,default=None)
    vendor_specific_property = models.CharField(max_length=100)
    store_deposit_account = models.CharField(max_length = 100 ,default='0000 0000 0000 0000')

    #user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES , default='vendor')

    class meta:
        verbose_name ='vendor'

    def __str__(self) -> str:
        return self.user.username


class Customer_info(models.Model):

    customer_specific_property = models.CharField(max_length=100)
    lives_in = models.CharField(max_length=50 ,default ='Algeria')
    #user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES , default='customer')

    class meta:
        verbose_name ='Customer'
        verbose_name_plural = 'Customers'