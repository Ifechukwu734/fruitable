from django.shortcuts import render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from shop.models import Billing_details, Ordered_products
# Create your views here.




def process_payments(request):
    host = request.get_host()
    order_id = request.session['order_id']
    billing_detail = Billing_details.objects.get(order_id = order_id)

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': billing_detail.total_order_price,
        'item_name': 'ordered product',
        'invoice': billing_detail.order_id,
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse('paypal-ipn')}',
        'return_url': f'http://{host}{reverse('payment_done')}',
        'cancel_return': f'http://{host}{reverse('payment_cancelled')}'
    }

    form = PayPalPaymentsForm(initial = paypal_dict)
    context = {
        'form': form,
        'billing_detail': billing_detail
    }
    return render(request,'pay.html', context )


@csrf_exempt
def payment_done(request):
    if 'cart_data_object' in request.session:
        del request.session['cart_data_object']
        del request.session['order_id']
    return render(request, 'success.html')


@csrf_exempt
def payment_cancelled(request):
    if 'cart_data_object' in request.session:
        del request.session['cart_data_object']
        del request.session['order_id']
    return render(request, 'fail.html')