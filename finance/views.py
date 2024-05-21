from django.shortcuts import render,redirect
from django.conf import settings
from store.models import Cart ,Product
from django.contrib.sessions.models import Session
from .models import *

from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import uuid

from accounts.views import timer

from .forms import CustomPaypalPaymentForm


from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED

# from chargily_epay_django import 



# Create your views here.

def the_total(sessionKey): 
    cart = Cart.objects.filter(session_id=sessionKey).last()
    cart_items =cart.cart_item_set.select_related('product').all()

    for item in cart_items:
        print(item.product.name,'   Q:',item.quantity)

    """
    check first if the item is still for sale and check the quantity ,
    if not satisfied delete the cart_item"""

    

    total = 0
    for item in cart_items:
        print(item.product.get_price())
        total =total +(item.product.get_price() *item.quantity)

    print('the total :',total)
    return total


def to_usd(price):
    return price/230


# _________________________



def payment_success(request):

    print('payment success')
    print('making the orders')

    if request.session.session_key == None:
        print('no session ,no orders made')

        return redirect(request,'')
    sessionKey = request.session.session_key


    cart = Cart.objects.filter(session_id=sessionKey).last()
    cart_items =cart.cart_item_set.select_related('product').all()

    # for item in cart_items:
    #     print(item.product.name,'   Q:',item.quantity)

    
    # we get the transaction

    this_transaction =Transaction.objects.filter(cart=cart).last()
    print(this_transaction.created_at)

    # making the new orders
    for item in cart_items:

        new_order = Order.objects.create(
            item=item.product,
            price_paid = item.product.get_price() *item.quantity,
            quantity =item.quantity,
            customer = this_transaction.customer,
            store =item.product.store,
            the_transaction=this_transaction ,

        )
        new_order.save()

    # now we put the transaction to complete
    this_transaction.status =transactionStatus.COMPLETED
    this_transaction.save()

    #then we make a new cart  ---> have to get sure if deleting the old will not result in bad stuff
    Cart.objects.create(session_id=sessionKey).save()


    return render(request ,'payment_success.html')



def payment_failed(request):

    return render(request ,'payment_failed.html')







@timer
def checkout_paypal(request):
    if request.session.session_key == None:
        return redirect(request,'')
    sessionKey = request.session.session_key


    cart = Cart.objects.filter(session_id=sessionKey).last()


    total_price =the_total(sessionKey)
    total_price_in_usd =to_usd(total_price)

    if request.user.is_authenticated:
        # the_user =User.objects.filter(username =request.user).first()
        
        new_transaction =Transaction.objects.create(
        cart=cart,
        total = total_price,
        customer =request.user,)
    else:
        new_transaction =Transaction.objects.create(
        cart=cart,
        total = total_price,
        )


    #we make a new transaction
    
    new_transaction.save()


    host = request.get_host()

    paypal_checkout = {
        'business':settings.PAYPAL_RECEIVER_EMAIL,
        'amount':total_price_in_usd,
        'item_name':'just trying',
        'invoice': new_transaction.id,
        'currency_code' :'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return': f"http://{host}{reverse('payment-success')}",
        'cancel': f"http://{host}{reverse('payment-failed')}",

    }

    paypal_form = PayPalPaymentsForm(initial=paypal_checkout)


    return render(request,'checkout.html',{'paypal':paypal_form})


@csrf_exempt
def paypal_webhook(sender ,**kwargs):
    """this views is not included yet """
    if sender.payment_status == ST_PP_COMPLETED:
        if sender.receiver_email == settings.PAYPAL_EMAIL:
            return None   #in case some one changes the hook and pays someone else and pretends  as if he payed
        else:
            print('payment success')
            # i did the rest above , 















# _________chargili__________

def checkout_chargili(request):
    pass





from chargily_epay_django.views import (
    CreatePaymentView ,
    PaymentConfirmationView,
    PaymentObjectDoneView ,
    FakePaymentView
    
    )
from .forms import PaymentForm


class CreatePayment(CreatePaymentView):
    template_name: str = "payment/payment-template.html"
    form_class = PaymentForm
    template_name ="chargily.html"


class PaymentConfirmation(PaymentConfirmationView):
    model = PaymentForm


class PaymentStatus(PaymentObjectDoneView):
    template_name: str = "payment/payment-status.html"
    model = PaymentForm


class FakePayment(FakePaymentView):
    model = PaymentForm



def chargilyWebhook(request):
    return render(request,"chargily/payment-success.html")