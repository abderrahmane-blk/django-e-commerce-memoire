from django.urls import path,include
from .views import *

urlpatterns = [
    path('' ,main_view ,name='main'),
    path('cart/' ,view_cart,name='cart'),
    path('cart/add/<str:pid>' ,add_to_cart,name='add to cart'),
    path('cart/remove/<str:pid>' ,remove_from_cart,name='remove from cart'),

    path('cart2/',view_cart_with_items , name='cart2'),
    path('cart2/del/<str:pid>' ,del_cart_item,name='del from cart2'),
    path('cart2/add/<int:pid>' ,add_cart_item,name='add cart2'),
    path('cart2/less/<int:pid>' ,less_of,name='less of'),
    path('cart2/more/<int:pid>' ,more_of,name='more of'),




]
