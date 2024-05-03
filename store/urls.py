from django.urls import path,include
from .views import *

urlpatterns = [
    # path('' ,main_view ,name='main'),  this was old

    #these are old
    # path('cart/' ,view_cart,name='cart'),
    # path('cart/add/<str:pid>' ,add_to_cart,name='add to cart'),
    # path('cart/remove/<str:pid>' ,remove_from_cart,name='remove from cart'),

    path('cart/',view_cart_with_items , name='cart'),
    path('cart/del/<str:pid>' ,del_cart_item,name='del from cart'),
    path('cart/add/<int:pid>' ,add_cart_item,name='add cart'),
    path('cart/less/<int:pid>' ,less_of,name='less of'),
    path('cart/more/<int:pid>' ,more_of,name='more of'),

# implementing the front end

    path('' ,app_main ,name='the main' ),
    path('product/<int:id>/' ,product_details,name='product'),

    path('dashboard/' ,dashboard ,name='dashboard'),
        path('dashboard/account/' , dashboard_account ,name='dashboard account'),
        path('dashboard/category/' ,dashboard_category ,name='dashboard category'),
        path('dashboard/products/' ,dashboard_products ,name='dashboard products'),
        path('dashboard/sellesdata/' ,dashboard_sellesdata ,name='dashboard sellesdata'),
        path('dashboard/settings/' ,dashboard_settings ,name='dashboard settings'),
        path('dashboard/users/' ,dashboard_users ,name='dashboard users'),



]
