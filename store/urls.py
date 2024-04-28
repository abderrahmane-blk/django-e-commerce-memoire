from django.urls import path,include
from .views import *

urlpatterns = [
    path('' ,main_view ,name='main'),

    #these are old
    # path('cart/' ,view_cart,name='cart'),
    # path('cart/add/<str:pid>' ,add_to_cart,name='add to cart'),
    # path('cart/remove/<str:pid>' ,remove_from_cart,name='remove from cart'),

    path('cart/',view_cart_with_items , name='cart'),
    path('cart/del/<str:pid>' ,del_cart_item,name='del from cart'),
    path('cart/add/<int:pid>' ,add_cart_item,name='add cart'),
    path('cart/less/<int:pid>' ,less_of,name='less of'),
    path('cart/more/<int:pid>' ,more_of,name='more of'),




]
