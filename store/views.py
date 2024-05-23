from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import *

from django.contrib.auth.decorators import login_required
    
from django.views.decorators.csrf import csrf_exempt 
from django.views.decorators.http import require_POST

from accounts.views import timer,is_permitted

from .forms import *
from finance.models import Order

from random import shuffle
from finance.models import OrderStatus



#usseless
@timer
def main_view(request):

    products= Product.objects.all()


    return render(request ,'mainstore.html',{'products':products} )



def the_comparator_items(request):
    """this function returns the products in the comparator of the session , if no session or no comparer it makes them"""
    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key
    
    products_in_comparer =None

    comparer = Comparer.objects.filter(session=session).first()
    if comparer is None:
        comparer = Comparer.objects.create(session_id=session)  

    products_in_comparer =comparer.comparer_product_set.select_related('product').all()


    return products_in_comparer


@timer
def del_comparer_item2(request,the_id):
    print('starting' ,the_id)
    print(request)
    
    product_item_to_del=Comparer_product.objects.filter(pk=the_id).first()
    product_item_to_del.delete()

    return JsonResponse({'message':'deleted'})


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

    if not request.session.session_key:
        request.session.create()
    session= request.session.session_key

    cart = Cart.objects.filter(session=session).last()
    if cart is None:
        cart = Cart.objects.create(session_id=session)  

    cart_items =cart.cart_item_set.select_related('product').all()

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
# the old version , now it is sent with the pages which requires it
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


# still
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

    return redirect(reverse('product',args=[pid]))

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

    is_permitted(request)

    categories = Category.objects.all()
    products = Product.objects.all()

    # for i in all_products:
    #     print(i)
    comparator_items =the_comparator_items(request)

    return render(request,'index.html',{'categories':categories , 'products': products,'comparator_items':comparator_items})

@timer
def product_details(request , id):
    the_product =Product.objects.filter(pk=id).first()
    comments =Comment.objects.filter(product=the_product).all()

    comparator_items =the_comparator_items(request)

    return render(request ,'productPage.html' ,{'product':the_product ,'comments':comments,'comparator_items':comparator_items})


@timer
def filter_page(request, cat_id=None):
    print(cat_id)
    products=None
    if request.method =='POST':
        
        min_price=request.POST.get('min_price')
        max_price=request.POST.get('max_price')

        if not min_price :
            min_price=0 
        if not max_price or max_price=="":
            max_price=90000000

    
        products = Product.objects.filter(category=cat_id).filter(price__gte=min_price,price__lte=max_price ).all().order_by('?')

    else:
        min_price=0 
        max_price=9000000
    if cat_id ==None:
        products = Product.objects.filter(price__gte=min_price,price__lte=max_price ).all().order_by('?')
    else:
        the_cate=Category.objects.filter(pk =cat_id).first()
        products = Product.objects.filter(price__gte=min_price,price__lte=max_price ,category=the_cate).all().order_by('?')

    # if not products:
    #     products = Product.objects.all().order_by('?')
    categories =Category.objects.all()

    return render(request,'FiltterPage.html' ,{'the_products':products,'categories':categories})




def filter_competetive(request,id):
    categories =Category.objects.all()

    the_product = Product.objects.filter(pk=id).first()
    max_price=the_product.price+1000

    name_competetives = Product.objects.filter(category=the_product.category).filter(name__icontains=the_product.name).filter(price__lte=max_price).all()
    sdescription_competetives = Product.objects.filter(category=the_product.category).filter(small_description__icontains=the_product.name).filter(price__lte=max_price).all()
    description_competetives = Product.objects.filter(category=the_product.category).filter(description__icontains=the_product.name).filter(price__lte=max_price).all()

    competetives =name_competetives.union(sdescription_competetives.union(description_competetives)).all()

    return render(request,'FiltterPage.html' ,{'the_products':competetives,'categories':categories})


@csrf_exempt
def add_comment(request ,product_id):
    theCommentForm =request.POST 
    product_commented =Product.objects.filter(pk=product_id).first()

    try:
        newComment =Comment.objects.create(content =theCommentForm['comment'] ,commentor=request.user ,product =product_commented)
        newComment.save()

    except:
        print('something happened')
    
    return redirect(reverse('product' ,args=[product_id]))










# ______________  all about the dashboard  _______________

def threat(request):
    return render(request ,'threat.html')









@timer
@login_required
def dashboard(request):
    if request.user.is_banned:
        return redirect(reverse('the main'))

    from django.db.models import Sum,Count
    sales= Order.objects.filter(order_status='sent',store__vendor =request.user).aggregate(sales_number=Count('price_paid'))['sales_number']
    earnings= Order.objects.filter(order_status='sent',store__vendor =request.user).aggregate(total_sales=Sum('price_paid'))['total_sales']
    if earnings is None :
        earnings=0

    recent_users =User.objects.order_by('date_joined').all()[0:10]
    recent_orders =Order.objects.order_by('created_on').all()[0:10]
    # print(earnings)
    # print(sales)
   

    return render(request,'dashboard/pages/dashboard.html' ,{'sales_number':sales,'total_paid':earnings,'recent_users':recent_users,'recent_orders':recent_orders})


@timer
def dashboard_account(request):
    user = request.user

    return render(request,'dashboard/pages/account.html')




# ____________dashboard CATEGORY____________
@timer
def dashboard_category(request,errors=[]):
    categories =Category.objects.all()

    return render(request,'dashboard/pages/category.html' ,{'categories':categories,'errors':errors})

@csrf_exempt
def delete_category(request,pk):

    # if request.user.is_superuser:
    if True:
    
        try:
            cate =Category.objects.filter(pk=pk).first()
            if cate == None:
                print('category does not exist')
                return JsonResponse({'message':'category does not exist'})

            cate.delete()
            print('deleted')
            return JsonResponse({'message':'category deleted'})

        except:
            print('something occured')
            return JsonResponse({'message':'not deleted'})
        
    else:
        return redirect(reverse('threat'))


@csrf_exempt
@require_POST
def add_category(request):
    new_category_name =request.POST['new_category_name']

    Category.objects.create(name=new_category_name).save()

    return redirect(reverse('dashboard category'))



@require_POST
@csrf_exempt  
def edit_category(request ,pk):
    errors=[]
    print(request.POST.get('new_name'))
    if request.POST.get('new_name')=="":
        errors.append('enter a name')

    new_name =None
    form = CategoryNameForm(data={'new_name' :request.POST.get('new_name')})
    if form.is_valid():
        new_name =form.cleaned_data['new_name']
        print('----------')
        print(new_name)
        print('----------')
    
    else:
        errors.append('enter a valid name')
        return dashboard_category(request,errors=errors)

    
    
    if Category.objects.filter(name=new_name).first():
        print('a category with this name already exists')
        return JsonResponse({'message':'a category with this name already exists'})
    else:
        cate = Category.objects.filter(pk=pk).first()
        cate.name =new_name
        cate.save()
        print('new name saved')
        # return JsonResponse({'message':'new name saved'})
    return dashboard_category(request,errors=errors)
    

#! dashboard Orders


def dashboard_orders(request):

    the_store = Store.objects.filter(vendor=request.user).first()
    the_orders =Order.objects.filter(store=the_store,).all()

    # {'categories':categories,'errors':errors}
    return render(request, "dashboard/pages/orders.html" ,{'orders':the_orders})


def accept_order(request,o_id):
    # check if this user is the store owner before
    the_order =Order.objects.filter(pk=o_id).first()
    the_order.order_status =OrderStatus.TO_BE_SENT
    the_order.save()

    return redirect(reverse('dashboard orders'))


def cancel_order(request,o_id):
    # check if this user is the store owner before
    the_order =Order.objects.filter(pk=o_id).first()
    the_order.order_status =OrderStatus.CANCELED
    the_order.save()

    return redirect(reverse('dashboard orders'))


def order_on_the_way(request,o_id):
    # check if this user is the store owner before
    the_order =Order.objects.filter(pk=o_id).first()
    the_order.order_status =OrderStatus.SENT
    the_order.save()

    return redirect(reverse('dashboard orders'))

def uncancel_order(request,o_id):
    # check if this user is the store owner before
    the_order =Order.objects.filter(pk=o_id).first()
    the_order.order_status =OrderStatus.WAITING
    the_order.save()

    return redirect(reverse('dashboard orders'))




# ?______________ products_______________
@timer
def dashboard_products(request):
    user = request.user
    store =Store.objects.filter(vendor=user.id).first()
    print(store)
    vendor_products =Product.objects.filter(store=store).all()
    cates =Category.objects.all()

    return render(request,'dashboard/pages/products.html' ,{'vendor_products':vendor_products,'categories':cates})


def edit_product(request,p_id):
    the_product =Product.objects.filter(pk=p_id).first()

    if request.method =='POST':
        the_form=ProductForm(request.POST)

        if the_form.is_valid():
            N_name =the_form.cleaned_data['name']
            N_small_description=the_form.cleaned_data['small_description']
            N_description=the_form.cleaned_data['description']
            N_price=the_form.cleaned_data['price']
            N_promotion_price=the_form.cleaned_data['promotion_price']
            # image=the_form.cleaned_data['image']
            N_quantity=the_form.cleaned_data['quantity']

            if N_name and N_name!='':
                the_product.name=N_name

            if N_small_description and N_small_description!='':
                the_product.small_description=N_small_description

            if N_description and N_description!='':
                the_product.description=N_description

            if N_price and N_price!='':
                the_product.price=N_price

            if N_promotion_price and N_promotion_price!='':
                the_product.promotion_price=N_promotion_price

            if N_quantity and N_quantity!='':
                the_product.quantity=N_quantity
            
            
            
        try:
            product_image =request.FILES['image']
            print(product_image)
            the_product.image=product_image

        except:
            pass
        
        the_product.save()



    return redirect(reverse('dashboard products'))



def add_new_product(request):
    if request.method=='POST':
        # the_product =Product.objects.filter(pk=p_id).first()
        the_form = NewProductForm(data={
            'name': request.POST.get('name'),
            'small_description': request.POST.get('small_description'),
            'description': request.POST.get('description'),
            'price': request.POST.get('price'),
            'promotion_price': request.POST.get('promotion_price'),
            'quantity': request.POST.get('quantity'),
        })
        print('------------')
        print('-----------a post request -------------')
        print('------------------------')

        if the_form.is_valid():
            print('form valid')
            N_name =the_form.cleaned_data['name']
            N_small_description=the_form.cleaned_data['small_description']
            N_description=the_form.cleaned_data['description']
            N_price=the_form.cleaned_data['price']
            if request.POST.get('promotion_price') and request.POST.get('promotion_price')!="":
                N_promotion_price=float(the_form.cleaned_data['promotion_price'])
            else:
                N_promotion_price=None
            N_quantity=the_form.cleaned_data['quantity']

            N_cate =int(request.POST.get('chosen_category'))
            N_cate =Category.objects.filter(pk=N_cate).first()

            # print('test')
            # print(N_name ,type(N_name))
            # print(N_small_description ,type(N_small_description))
            # print(N_description ,type(N_description))
            # print(N_price ,type(N_price))
            # print(N_promotion_price ,type(N_promotion_price))
            # print(N_quantity ,type(N_quantity))

            


            the_user =User.objects.filter(pk=request.user.pk).first()
            created =False
            the_store=Store.objects.filter(vendor=request.user).first()
            if N_name and N_name!='':
                # print('-----------1-------------')
                if N_small_description and N_small_description!='':
                    # print('-----------2-------------')
                    if N_description and N_description!='':
                        # print('-----------3-------------')
                        if N_price and N_price!='':
                            # print('-----------4-------------')

                            if N_quantity and N_quantity!='':
                                print(N_promotion_price)
                                if N_promotion_price !="": 
                                    the_product =Product.objects.create(name=N_name,
                                                                        small_description=N_small_description,
                                                                        description=N_description,
                                                                        price=N_price,
                                                                        quantity=N_quantity,
                                                                        owner=the_user,
                                                                        store =the_store,
                                                                        category=N_cate,
                                                                        )
                                    the_product.promotion_price=N_promotion_price

                                    created=True
                                    
                                    # print(type(the_product))
                                    # print(the_product)

                                else:
                                    the_product =Product.objects.create(name=N_name,
                                                                    small_description=N_small_description,
                                                                    description=N_description,
                                                                    price=N_price,
                                                                    quantity=N_quantity,
                                                                    owner=the_user,
                                                                    store =the_store,
                                                                    )
                                    created=True
                                    # print(type(the_product))
                                    # print(the_product)


                                
            try:
                # print('now the image')
                product_image =request.FILES['image']
                print(product_image)
                if created:
                    try:
                        the_product.image=product_image
                    except:
                        pass

            except:
                pass
        
            the_product.save()

    return redirect(reverse('dashboard products'))


def del_product(request,pid):
    try:
        prod =Product.objects.filter(pk=pid).first()
        if prod == None:
            print('products does not exist')
            return JsonResponse({'message':'product does not exist'})

        prod.delete()
        print('deleted')
        return JsonResponse({'message':'product deleted'})

    except:
        print('something occured')
    return JsonResponse({'message':'not deleted'})




# ____dashboard selles data

@timer
def dashboard_sellesdata(request):
    who ='all'
    if request.user.is_superuser:
        filters ={}
        vendor_name =request.GET.get('vendor',None)
        if vendor_name:
            who =''
            vendor =User.objects.filter(username__icontains=vendor_name).all()
            the_store =Store.objects.filter(vendor__in=vendor).all()

            filters['store__in']=the_store
        
        orders = Order.objects.filter(**filters).select_related('store','store__vendor').order_by('-created_on').all()

    else:
        the_store =Store.objects.filter(vendor=request.user).first()
        orders = Order.objects.select_related('store','store__vendor').order_by('-created_on').filter(store=the_store,order_status='sent').all()


    return render(request,'dashboard/pages/sellesdata.html' ,{'orders':orders ,'who':who})





@timer
def dashboard_settings(request):
    user = request.user

    return render(request,'dashboard/pages/settings.html')

@timer
def dashboard_users(request):
    user = request.user
    users =User.objects.all()

    def usertype(self):
        if self.is_superuser:
            return 'superuser'
        elif True:
            v =Vendor_info.objects.filter(user=self.pk).first()
            if v is None:
                pass
            else: return 'vendor'
        
        return 'customer'

    for user in users:
        user.type = usertype(user)


    

    return render(request,'dashboard/pages/users.html' ,{'users':users})


def userban(request,u_id):
    
    if not request.user.is_superuser:
        return redirect(reverse('dashboard'))
    
    the_user=User.objects.filter(pk=u_id).first()
    print('banning ')
    the_user.is_banned=True
    the_user.is_active=False
    the_user.save()

    return redirect(reverse('dashboard users'))


def user_reautherize(request,u_id):
    if not request.user.is_superuser:
        return redirect(reverse('dashboard'))

    the_user=User.objects.filter(pk=u_id).first()
    print('re autherizing ')
    the_user.is_banned=False
    the_user.is_active=True
    the_user.save()

    return redirect(reverse('dashboard users'))










def filter_page__try(request):
    return render(request,'FiltterPage.html')


def try_compare(request):
    return render(request,'components/comparator.html')

def get_comparer_data(request):
    co_items =Comparer_product.objects.filter('comparer__session'=='vigy63yssnksm4689yu5pigu2xvefcin').all()
    print(co_items)
    return JsonResponse({'message':None})







def django_admmin(request):
    return redirect(reverse('the admin')) 