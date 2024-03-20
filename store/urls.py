from django.urls import path,include
from .views import *

urlpatterns = [
    path('' ,main_view ,name='main'),
    path('cart/' ,view_cart,name='cart'),
    path('cart/add/<str:pid>' ,add_to_cart,name='add to cart'),
    path('cart/remove/<str:pid>' ,remove_from_cart,name='remove from cart')



]
