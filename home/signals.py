from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Otp_token_generator
from django.conf import settings


@receiver(post_save, sender=User)
def otp_token(instance, sender, created, **kwargs):
    if created:
        if instance.is_superuser:
            pass
        else:
            otp = Otp_token_generator.objects.create(user=instance, date_expired = timezone.now() + timezone.timedelta(seconds=50))
            instance.is_active = False
            otp.save()

        new_otp_token = Otp_token_generator.objects.filter(user = instance).last()

        subject = 'Email Verification'
        message = f'''
            Dear {instance.username}, 

            This is your Email Verification Code {new_otp_token}
         '''
        from_email= settings.EMAIL_HOST_USER
        receiver = [instance.email]

        send_mail(subject, message, from_email, receiver, fail_silently=False)
        
        