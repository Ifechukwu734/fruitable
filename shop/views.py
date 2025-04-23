from django.shortcuts import render, redirect
from .models import Product_category,  Products, Comment, Featured_products, Ordered_products, Billing_details
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
# Create your views here.

def shop_page(request):
    product = Products.objects.all()
    paginator = Paginator(product, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)    
    product_categories = Product_category.objects.all()
    featured_products = Featured_products.objects.filter(display_on_sidebar = True)
    list = ['Organic', 'Fresh', 'Sales', 'Discount', 'Expired']
  
    context = {
       'products': page_obj,
       'product_category': product_categories,
       'list': list,
       'featured_products': featured_products
    }
    return render(request, 'shop.html', context)


def product_details(request, name, product_id):
    product_detail = Products.objects.get(id=product_id)
    category = product_detail.product_category
    featured_products = Featured_products.objects.filter(display_on_sidebar = True)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('user-email')
        comment = request.POST.get('comments')
        image = request._files.get('images')                   

        new_comment = Comment.objects.create(name = name, email = email, comment = comment, post = product_detail, comment_image = image )
        new_comment.save()
        return redirect('/shop/')
    
    shop = Products.objects.filter(product_category = category)
    post_comment = product_detail.comment_set.all()
    context = {
        'product': product_detail,
        'shop': shop,
        'post_comments': post_comment,
        'featured_products': featured_products
    }
    return render(request, 'product_details.html', context)


def filter_product(request):
    message = ''
    name = request.GET.get('search')
    range = request.GET.get('range')
    checked = request.GET.get('checked')
    product = Products.objects.filter(product_name__icontains=name,price=range)
    if checked != None:
        product = Products.objects.filter(product_name__icontains=name,price=range,product_quality__icontains=checked)
    if not product.exists():
        message = 'product unavailable'        
    products = render_to_string('filter.html', {'products': product})
    filter = render_to_string('product unavailable.html', {'messages': message})
    data = {
        'product': products,
        'message': str(message),
        'filter': filter      
    }

    return JsonResponse(data=data)
    

def add_to_cart(request):
    product_id = str(request.GET.get('product_id'))
    product_name = str(request.GET.get('product_name'))
    quantity = int(request.GET.get('quantity'))
    price = int(request.GET.get('price'))
    image = request.GET.get('image')

    cart_product = {}
    cart_product[str(product_id)] = {
        'name': product_name,
        'price': price,
        'quantity': quantity,
        'image': image
    }
    

    if 'cart_data_object' in request.session:
        if str(product_id) in request.session['cart_data_object']:
            cart_data = request.session['cart_data_object']
            cart_data[str(product_id)]['quantity'] = int(cart_product[str(product_id)]['quantity'])
            cart_data.update(cart_data)
            request.session['cart_data_object'] = cart_data
        else:
            cart_data = request.session['cart_data_object']
            cart_data.update(cart_product)
            request.session['cart_data_object'] = cart_data
    else:
        request.session['cart_data_object'] = cart_product
        request.session['order_id'] = str(uuid.uuid4())

    data = {
        'length': len(request.session['cart_data_object']),
        'session': request.session['cart_data_object']
    }
    return JsonResponse(data=data)


def add_featured_product_to_cart(request):
    product_id = request.GET.get('product_id')
    product_name = str(request.GET.get('product_name'))
    quantity = int(request.GET.get('quantity'))
    price = int(request.GET.get('price'))
    image = request.GET.get('image')

    cart_product = {}
    cart_product[str(product_id)] = {
        'name': product_name,
        'price': price,
        'quantity': quantity,
        'image': image
    }

    if 'cart_data_object' in request.session:
        if str(product_id) in request.session['cart_data_object']:
            cart_data = request.session['cart_data_object']
            cart_data[str(product_id)]['quantity'] = int(cart_product[str(product_id)]['quantity'])
            cart_data.update(cart_data)
            request.session['cart_data_object'] = cart_data
        else:
            cart_data = request.session['cart_data_object']
            cart_data.update(cart_product)
            request.session['cart_data_object'] = cart_data
    else:
        request.session['cart_data_object'] = cart_product
        request.session['order_id'] = str(uuid.uuid4())

    data = {
        'length': len(request.session['cart_data_object']),
        'session': request.session['cart_data_object']
    }
    return JsonResponse(data=data)



def cart_items(request):
    total_price = 0
    if 'cart_data_object' in request.session:
        for id, item in request.session['cart_data_object'].items():
            total_price += int(item['quantity']) * float(item['price'])
        final_price = total_price + 3
    else:
        messages.warning(request, 'Your cart is empty')
        return redirect('/')
    
    context = {
        'session': request.session['cart_data_object'],
        'total_object': total_price,
        'final_price': final_price
    }
    return render(request, 'cart.html', context)


def delete_item(request):
    product_id = str(request.GET.get('product_id'))
    if 'cart_data_object' in request.session:
        if product_id in request.session['cart_data_object']:
            cart = request.session['cart_data_object']
            del cart[product_id]
            request.session['cart_data_object'] = cart

    total_price = 0
    if 'cart_data_object' in request.session:
        for id, items in request.session['cart_data_object'].items():
            total_price += int(items['quantity']) * float(items['price'])
        final_price = total_price + 3
      
    context = render_to_string('cart list.html', {'final_price': final_price,'cart_data': request.session['cart_data_object'], 'total_items': len(request.session['cart_data_object']), 'total_price': total_price})
    data = {
        'context': context
    }
    return JsonResponse(data=data)


def reload(request):
    product_id = str(request.GET.get('product_id'))
    quantity = int(request.GET.get('quantity'))
    
    if 'cart_data_object' in request.session:
        if product_id in request.session['cart_data_object']:
            cart_data = request.session['cart_data_object']
            cart_data[product_id]['quantity'] = quantity
            cart_data.update(cart_data)
            request.session['cart_data_object'] = cart_data

    if 'cart_data_object' in request.session:
        total_price = 0
        for id, item in request.session['cart_data_object'].items():
            total_price += int(item['quantity']) * float(item['price'])
        final_price = total_price + 3
    

    context = render_to_string('cart list.html', {'final_price': final_price,'cart_data': request.session['cart_data_object'], 'total_items': len(request.session['cart_data_object']), 'total_price': total_price})
    data = {
        'context': context
    }
    return JsonResponse(data=data)

    
def featured_products(request):
    featured_products = Featured_products.objects.all()
    paginator = Paginator(featured_products, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    list = ['Organic', 'Fresh', 'Sales', 'Discount', 'Expired']
    context = {
        'featured_products': page_obj,
        'list': list
    }
    return render(request, 'featured products.html', context)


def filter_featured_product(request):
    message = ''
    name = request.GET.get('search')
    range = request.GET.get('range')
    checked = request.GET.get('checked')
    product = Featured_products.objects.filter(product_name__icontains=name,featured_price=range)
    if checked != None:
        product = Featured_products.objects.filter(product_name__icontains=name,featured_price=range,product_quality__icontains=checked)
    if not product.exists():
        message = 'product unavailable'        
    products = render_to_string('filter featured products.html', {'products': product})
    unavailable = render_to_string('featured product unavailable.html',{'messages': message})
    data = {
        'product': products,
        'message': str(message),
        'unavailable': unavailable      
    }

    return JsonResponse(data=data)


def featured_details(request, name, id):
    products = Featured_products.objects.get(id=id)
    context = {
        'product': products
    }
    return render(request, 'featured details.html', context)


def checkout(request):
    cart_data = request.session['cart_data_object']
    session_id = request.session['order_id']
    sub_total = 0
    

    for id, items in cart_data.items():
        sub_total += int(items['price']) * float(items['quantity'])
    
    total_items = sub_total + 15

    if request.method == 'POST':
        order_id = session_id
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        town = request.POST.get('town')
        country = request.POST.get('country')
        postcode = request.POST.get('postcode')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        order_notes = request.POST.get('order_notes')
        total_item = request.POST.get('total_items')
        local_pickup = request.POST.get('Shipping-1')

        if local_pickup:
            local_pickup = True
        else:
            local_pickup = False

        if order_notes == 'None':
            order_notes = ''
        
        billing_detail = Billing_details.objects.create(order_id = order_id, first_name = first_name, last_name = last_name, company_name = company_name,
                                                        address = address, town = town, country = country, post_code = postcode, mobile_number = mobile,
                                                        email = email, order_notes = order_notes, local_pickup = local_pickup, total_order_price = total_item, 
                                                        total_items = len(request.session['cart_data_object']),paid = False)
        billing_detail.save()

        for id, item in cart_data.items():
            ordered_product = Ordered_products.objects.create(order_id = order_id, product_id = id, product_name = item['name'], 
                                                              product_image = item['image'], product_price = item['price'], product_quantity = item['quantity'],
                                                              total_order_price = total_item, paid = False)
            ordered_product.save()
        return redirect('pay/')
    
    context = {
        'total_items': total_items,
        'sub_total': sub_total
    }
    return render(request, 'checkout.html', context)


def local_pickup(request):
    message = request.GET.get('message')
    cart_data = request.session['cart_data_object']
    sub_total = 0
    new_total = 0

    for id, items in cart_data.items():
        sub_total += int(items['price']) * float(items['quantity'])
    
    total_items = sub_total + 15
    
    if message == 'checked':
        new_total = total_items + 8
    elif message == 'unchecked':
        new_total = total_items
    
    data = {
        'new_total': new_total
    }

    return JsonResponse(data=data)


