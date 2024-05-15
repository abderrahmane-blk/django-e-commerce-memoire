from django.urls import path,include
from .views import *

#for media


urlpatterns = [
    path('checkout/' ,checkout_paypal ,name='checkout' ),

    path('success-payment/' ,payment_success ,name='payment-success' ),
    path('failed-payment/' ,payment_failed ,name='payment-failed' ),
    path('paypal/' ,include('paypal.standard.ipn.urls')),



]