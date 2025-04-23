from django.dispatch import receiver
from shop.models import Billing_details
from paypal.standard.ipn.signals import valid_ipn_received


@receiver(valid_ipn_received)
def notification(sender, **kwargs):
    ipn = sender
    order_id = ipn.invoice
    if ipn.payment_status == 'Completed':
        new_order = Billing_details.objects.get(order_id = order_id)
        new_order.paid = True
        new_order.save()
