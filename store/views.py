from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import *
# Create your views here.






def main_view(request):

    products= Product.objects.all()


    return render(request ,'mainstore.html',{'products':products} )


# cart views

#here 
#deleting sessions

#to be deleted
def view_cart(request):
    if not request.session:
        request.session.create()
    session= request.session._get_session_from_db()


    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        cart = Cart.objects.create(session=session)  

    for a,b in cart.items.items():
        print( str(a)+' has '+str(b) )
    

    products_in_cart =Product.objects.filter(pk__in=cart.items.keys())

    return render(request ,'cart.html' ,{'cart':cart ,'products_in_cart':products_in_cart})



def add_to_cart(request ,pid):
    if not request.session:
        request.session.create()
    session_key = request.session._get_session_from_db()
    print(request.session)

    cart = Cart.objects.filter(session=session_key).last()

    if cart is None:
        cart = Cart.objects.create(session=session_key ,items=[pid,])
    else:
        print(cart.items)
        cart.items[pid]=1
        cart.save()# again , do not forget to save after append
    
    #return render(request ,'cart.html' ,{'cart':cart})
    return JsonResponse({
            'message':'added successfully',
            'items_count':len(cart.items),
        }) 


def remove_from_cart(request ,pid):
    if not request.session:
        return JsonResponse({}) 

    session_key = request.session._get_session_from_db()


    cart = Cart.objects.filter(session=session_key).last()

    if cart is None:
        return JsonResponse({}) 


    else:
        print(cart.items)
        del cart.items[pid]
        print(cart.items)

        cart.save()# again , do not forget to save after append
    
    #return render(request ,'cart.html' ,{'cart':cart})
    return JsonResponse({
            'message':'deleted from cart successfully',
            'items_count':len(cart.items),
        }) 








# cart with items


def view_cart_with_items(request):

    # print('----------')    
    # print('----------')
    # print(request.session)
    # print(request.session.session_key)
    # print('----------')
    print('-----1-----')


    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key
    # print('-----2-----')


    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        cart = Cart.objects.create(session_id=session)  

    cart_items =cart.cart_item_set.select_related('product').all()

    # print('-----3-----')

    return render(request ,'cart_items.html' ,{'cart':cart ,'cart_items':cart_items })




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

    return redirect('cart2')

    """later the return should be changed to this
        return JsonResponse({
                'message':'added successfully',
                'items_count':items_in_cart,
            }) 
    """



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
    item.save()

    if a<=0:
        """delete


          item 


          here
        """
        pass


    items_in_cart =cart.cart_item_set.count() 
    print(items_in_cart)

    return redirect(view_cart_with_items)

    """later the return should be changed to something like this for better performance
            return JsonResponse({})
    """


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








