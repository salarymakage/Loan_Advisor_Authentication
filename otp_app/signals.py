# otp_app/signals.py

from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import OtpToken
from django.core.mail import send_mail
from django.utils import timezone

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        otp = OtpToken.objects.create(user=instance, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
        instance.is_active = False
        instance.save()

        # Email credentials
        subject = "Email Verification"
        message = f"""
        Hi {instance.username}, here is your OTP {otp.otp_code}
        It expires in 5 minutes. Use the URL below to redirect back to the website:
        http://127.0.0.1:8000/verify-email/{instance.username}
        """
        sender_email = "clintonmatics@gmail.com"
        receiver = [instance.email]

        # Send email
        send_mail(
            subject,
            message,
            sender_email,
            receiver,
            fail_silently=False,
        )
