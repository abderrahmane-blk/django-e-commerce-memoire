from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.






def main_view(request):

    products= Product.objects.all()


    return render(request ,'mainstore.html',{'products':products} )


# cart views

#here 
#deleting sessions


def view_cart(request):
    if not request.session:
        request.session.create()
    session= request.session._get_session_from_db()

    print(request.session)
    print(session)
    print('-----')
    print('-----')
    print('-----')


    cart = Cart.objects.filter(session=session).last()
    print('working to here') 


    if cart is None:
        cart = Cart.objects.create(session=session)  

    print('working to here2') 

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










