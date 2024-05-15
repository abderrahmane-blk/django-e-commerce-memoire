from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import *

from django.contrib.auth.decorators import login_required
# Create your views here.
from accounts.views import timer





@timer
def main_view(request):

    products= Product.objects.all()


    return render(request ,'mainstore.html',{'products':products} )


# cart views

#here 
#deleting sessions

#to be deleted
# def view_cart(request):
#     if not request.session:
#         request.session.create()
#     session= request.session._get_session_from_db()


#     cart = Cart.objects.filter(session=session).last()
#     if cart is None:
#         cart = Cart.objects.create(session=session)  

#     for a,b in cart.items.items():
#         print( str(a)+' has '+str(b) )
    

#     products_in_cart =Product.objects.filter(pk__in=cart.items.keys())

#     return render(request ,'cart.html' ,{'cart':cart ,'products_in_cart':products_in_cart})



# def add_to_cart(request ,pid):
#     if not request.session:
#         request.session.create()
#     session_key = request.session._get_session_from_db()
#     print(request.session)

#     cart = Cart.objects.filter(session=session_key).last()

#     if cart is None:
#         cart = Cart.objects.create(session=session_key ,items=[pid,])
#     else:
#         print(cart.items)
#         cart.items[pid]=1
#         cart.save()# again , do not forget to save after append
    
#     #return render(request ,'cart.html' ,{'cart':cart})
#     return JsonResponse({
#             'message':'added successfully',
#             'items_count':len(cart.items),
#         }) 


# def remove_from_cart(request ,pid):
#     if not request.session:
#         return JsonResponse({}) 

#     session_key = request.session._get_session_from_db()


#     cart = Cart.objects.filter(session=session_key).last()

#     if cart is None:
#         return JsonResponse({}) 


#     else:
#         print(cart.items)
#         del cart.items[pid]
#         print(cart.items)

#         cart.save()# again , do not forget to save after append
    
#     #return render(request ,'cart.html' ,{'cart':cart})
#     return JsonResponse({
#             'message':'deleted from cart successfully',
#             'items_count':len(cart.items),
#         }) 







# cart with items

@timer
def view_cart_with_items(request):

    # print('-----1-----')


    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key
    # print('-----2-----')


    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        cart = Cart.objects.create(session_id=session)  

    cart_items =cart.cart_item_set.select_related('product').all()

    # print('-----3-----')
    the_total = 0
    for item in cart_items:
        the_total =the_total +(item.product.get_price() *item.quantity)


    return render(request ,'cart_items.html' ,{'cart':cart ,'cart_items':cart_items,'total':the_total })

@timer
def add_cart_item(request ,pid):
    
    # print('-----add1-----')

    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key

    # print('-----add2-----')

    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        cart = Cart.objects.create(session_id=session)  
        """note : here we used the parameter session_id which is not in our cart model ,this means we made a session and then returned the session instance here"""
    product_to_add =Product.objects.filter(pk=pid).first()
    # print('-----add3-----')


    
    if product_to_add is None:
        return JsonResponse({
            'message':'this product does not exist anymore',
        }) 
    
    if Cart_item.objects.filter(cart=cart,product=product_to_add):
        items_in_cart =cart.cart_item_set.count() 
        return JsonResponse({
            'message':'already in cart',
            'items_count':items_in_cart,
        })

    Cart_item.objects.create(
        cart=cart,
        product=product_to_add
    )
    # print('-----add4-----')

    items_in_cart =cart.cart_item_set.count() 
    print(items_in_cart)

    #return redirect(view_cart_with_items)
    return redirect(reverse('cart')) 

    """later the return should be changed to this
        return JsonResponse({
                'message':'added successfully',
                'items_count':items_in_cart,
            }) 
    """



#prblem here ^^^^^ fix it


@timer
def more_of(request,pid):
    """this function adds 1 more to the quantity of a cart item"""

    """session is checked incase someone tries to add more to a deleted session"""
    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key


    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        cart = Cart.objects.create(session_id=session)  


    product_to_add_quantity =Product.objects.filter(pk=pid).first()


    
    if product_to_add_quantity is None:
        return JsonResponse({
            'message':'this product does not exist anymore',
        }) 


    item=Cart_item.objects.filter(
        cart=cart,
        product=product_to_add_quantity
    ).first()
    item.quantity=item.quantity+1
    item.save()

    items_in_cart =cart.cart_item_set.count() 
    print(items_in_cart)


    return redirect(view_cart_with_items)


    """later the return should be changed to something like this for better performance
            return JsonResponse({})
    """


@timer
def less_of(request,pid):
    """this function substracts 1 from the quantity of a cart item  :if reached 0 -> item is deleted"""

    """session is checked incase someone tries to substracts from a deleted session"""
    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key


    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        cart = Cart.objects.create(session_id=session)  

    product_to_substract_quantity =Product.objects.filter(pk=pid).first()


    
    if product_to_substract_quantity is None:
        return JsonResponse({
            'message':'this product does not exist anymore',
        }) 

    item=Cart_item.objects.filter(
        cart=cart,
        product=product_to_substract_quantity
    ).first()
    a=item.quantity=item.quantity-1


    if not a<=0:
        """
        nothing happens

        """
        item.save()


    items_in_cart =cart.cart_item_set.count() 
    print(items_in_cart)

    return redirect(view_cart_with_items)

    """later the return should be changed to something like this for better performance
            return JsonResponse({})
    """

@timer
def del_cart_item(request,pid):
    
    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key


    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        return JsonResponse({})
    product =Product.objects.filter(pk=pid).first()
    product_item_to_del=Cart_item.objects.filter(cart=cart,product=product).first()
    product_item_to_del.delete()

    return JsonResponse({'message':'deleted'})


# ___________________  Comparer  _____________________
@timer
def comparer(request):
    
    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key

    comparer = Comparer.objects.filter(session=session).first()
    if comparer is None:
        comparer = Comparer.objects.create(session_id=session)  

    products_in_comparer =comparer.comparer_product_set.select_related('product').all()


    return render(request ,'comparer.html',{'comparer':comparer,'products_in_comparer':products_in_comparer})


@timer
def add_comparer_item(request ,pid):
    
    # print('-----add1-----')

    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key

    print('-----sessioned-----')

    comparer = Comparer.objects.filter(session=session).first()
    if comparer is None:
        comparer = Comparer.objects.create(session_id=session)  
        """note : here we used the parameter session_id which is not in our cart model ,this means we made a session and then returned the session instance here"""
    product_to_add =Product.objects.filter(pk=pid).first()
    print('-----2-----')


    
    if product_to_add is None:
        return JsonResponse({
            'message':'this product does not exist anymore',
        }) 
    
    if Comparer_product.objects.filter(comparer=comparer,product=product_to_add):
        items_in_comparer =comparer.comparer_product_set.count() 
        return JsonResponse({
            'message':'already in comparer',
            'items_count':items_in_comparer,
        })

    Comparer_product.objects.create(
        comparer=comparer,
        product=product_to_add
    )
    print('-----added-----')

    items_in_comparer =comparer.comparer_product_set.count() 
    print('we have in  the comparer ::: '+str(items_in_comparer))

    return redirect(reverse('comparer'))

    """later the return should be changed to this
        return JsonResponse({
                'message':'added successfully',
                'items_count':items_in_comparer,
            }) 
    """


@timer
def del_comparer_item(request,pid):
    
    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key

    comparer = Comparer.objects.filter(session=session).last()
    if comparer is None:
        return JsonResponse({'hi':'there'})
    product =Product.objects.filter(pk=pid).first()
    product_item_to_del=Comparer_product.objects.filter(comparer=comparer,product=product).first()
    product_item_to_del.delete()

    return JsonResponse({'message':'deleted'})

# __________________________________________





# ________________________ implementing the front end _________________________
@timer
def app_main(request):

    categories = Category.objects.all()
    products = Product.objects.all()

    # for i in all_products:
    #     print(i)


    return render(request,'index.html',{'categories':categories , 'products': products})

@timer
def product_details(request , id):
    product =Product.objects.filter(pk=id).first()
    print(product)

    return render(request ,'productPage.html' ,{'product':product})




# ______________  all about the dashboard  _______________
@timer
@login_required
def dashboard(request):
    user = request.user
   

    return render(request,'dashboard/pages/dashboard.html')


@timer
def dashboard_account(request):
    user = request.user

    return render(request,'dashboard/pages/account.html')


@timer
def dashboard_category(request):
    user = request.user
    categories =Category.objects.all()

    return render(request,'dashboard/pages/category.html' ,{'categories':categories})

@timer
def dashboard_products(request):
    user = request.user
    store =Store.objects.filter(vendor=user.id).first()
    vendor_products =Product.objects.filter(store=store.id).all()

    return render(request,'dashboard/pages/products.html' ,{'vendor_products':vendor_products})

@timer
def dashboard_sellesdata(request):
    user = request.user

    return render(request,'dashboard/pages/sellesdata.html')

@timer
def dashboard_settings(request):
    user = request.user

    return render(request,'dashboard/pages/settings.html')

@timer
def dashboard_users(request):
    user = request.user
    users =User.objects.all()

    return render(request,'dashboard/pages/users.html' ,{'users':users})





def filter_page__try(request):
    return render(request,'filter_page.html')