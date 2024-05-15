
from django import forms
from django.utils.html import format_html

from paypal.standard.forms import PayPalPaymentsForm




class CustomPaypalPaymentForm(PayPalPaymentsForm):

    def render(self ,*args,**kwargs):
        return format_html(u"""<form action="{0}" method="post">
                           {1}
                                    <div class="d-grid gap-2 my-3" >
                                        <button  class="btn btn-primary" type="submit">
                                            <i class="lni lni-paypal-original" ></i> {2}
                                        </button>
                                    </div>
                           </form>
         """, self.get_login_url(), self.as_p(),"pay with Paypal or credit card" )
    










