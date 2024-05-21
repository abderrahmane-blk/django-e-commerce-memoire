from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_TYPE_CHOICES = (
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
    )


class Vendor_info(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)

    bio = models.CharField(max_length = 255 ,null=True ,default=None)
    #user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES , default='vendor')

    class meta:
        verbose_name ='vendor'

    def __str__(self) -> str:
        return self.user.username


class Customer_info(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE ,null=True)
    lives_in = models.CharField(max_length=50 ,default ='Algeria')
    image =models.ImageField( upload_to='users' ,null=True,blank=True, height_field=None, width_field=None, max_length=None)

    class meta:
        verbose_name ='Customer'
        verbose_name_plural = 'Customers'