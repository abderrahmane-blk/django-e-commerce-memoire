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

    # the comparer routes
    path('comparer/',comparer , name='comparer'),
    path('comparer/add/<int:pid>' ,add_comparer_item,name='add to comparer'),
    path('comparer/del/<str:pid>' ,del_comparer_item,name='del from comparer'),

    path('filtertry/' ,filter_page__try,name='filter try'),
    path('filter/' ,filter_page,name='filter'),
    path('filter/<int:cat_id>' ,filter_page,name='cat filter'),
    path('competetives/<int:id>' ,filter_competetive,name='competetives'),







# implementing the front end

    path('' ,app_main ,name='the main' ),
    path('product/<int:id>/' ,product_details,name='product'),

    path('dashboard/' ,dashboard ,name='dashboard'),
        path('dashboard/account/' , dashboard_account ,name='dashboard account'),
        path('dashboard/category/' ,dashboard_category ,name='dashboard category'),
            path('dashboard/category/add/' ,add_category ,name='new category'),
            path('dashboard/category/del/<int:pk>' ,delete_category ,name='del category'),
            path('dashboard/category/edit/<int:pk>/' ,edit_category ,name='edit category'),


        path('dashboard/products/' ,dashboard_products ,name='dashboard products'),
        path('dashboard/products/add/' ,add_new_product ,name='add product'),
        path('dashboard/product/edit/<int:p_id>/' ,edit_product ,name='edit product'),
        path('dashboard/product/del/<int:pid>' ,del_product ,name='del product'),


        path('dashboard/sellesdata/' ,dashboard_sellesdata ,name='dashboard sellesdata'),
        path('dashboard/settings/' ,dashboard_settings ,name='dashboard settings'),
        path('dashboard/users/' ,dashboard_users ,name='dashboard users'),



    path('threat/' ,threat ,name='threat'),
    path('comment/<int:product_id>' ,add_comment ,name='comment'),
    path('compar/' ,try_compare ,name='co'),
    path('comparD/' ,get_comparer_data ,name='get comparer data'),
    path('compar/del/<int:the_id>' ,del_comparer_item2 ,name='get comparer data'),




]
