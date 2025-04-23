from django.shortcuts import render, redirect
from .models import Index_page, First_slider, Second_slider, Sign_up_image
from shop.models import Products, Comment, Featured_products
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    index_page = Index_page.objects.all()
    first_slider = First_slider.objects.all()
    second_slider = Second_slider.objects.all()
    organic_products = Products.objects.filter(product_quality__icontains = 'Organic')
    vegetables = Products.objects.filter(product_quality__icontains = 'Organic', product_category__name = 'Vegetables')
    Fruits = Products.objects.filter(product_quality__icontains = 'Organic', product_category__name = 'Fruits')
    Bread = Products.objects.filter(product_quality__icontains = 'Organic', product_category__name = 'Bread')
    Meat = Products.objects.filter(product_quality__icontains = 'Organic', product_category__name = 'Meat')
    fresh_vegetables = Products.objects.filter(product_quality__icontains = 'Fresh', product_category__name = 'Vegetables')
    best_seller = Products.objects.filter(best_seller = True)
    comment = Comment.objects.all()

    context = {
        'index_page': index_page,
        'first_slider': first_slider,
        'second_slider': second_slider,
        'organic_products': organic_products,
        'vegetables': vegetables,
        'fruits': Fruits,
        'bread': Bread,
        'meat': Meat,
        'fresh_vegetables': fresh_vegetables,
        'best_seller': best_seller,
        'comment': comment
    }
    return render(request, 'index.html', context)


def search(request):
    message = ''
    name = request.GET.get('searchKeyword')
    featured_products = Featured_products.objects.filter(display_on_sidebar = True)
    products = Products.objects.filter(product_name__icontains = name)
    if not products.exists():
        message = 'Product is not available'
    context = {
        'products': products,
        'featured_products': featured_products,
        'message': message
    }    
    return render(request, 'search result.html', context)


def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username)
        if password1 == password2:
            if not User.objects.filter(email=email).exists():
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(first_name=full_name, username=username, email=email, password=password1)
                    user.save()
                    
                    return redirect('signup/verify/')
                else:
                    messages.info(request, 'Username is taken')
                    return redirect(request.path)
            else:
                messages.info(request, 'Email already exists')
                return redirect(request.path)
        else:
            messages.warning(request, "password don't match ")
            return redirect(request.path)

    img = Sign_up_image.objects.all()
    context = {
        'image': img
    }
    return render(request, 'sign_up.html', context)


def verify(request):
    return render(request, 'verify.html')
