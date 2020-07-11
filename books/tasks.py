from celery import shared_task
from django.core.mail import EmailMultiAlternatives

from books.helper import get_email_message
from books.models import Order


@shared_task
def order_book(order_id):
    try:
        order = Order.objects.select_related('book', 'client').get(id=1)
    except Order.DoesNotExist:
        return

    message = get_email_message(order)

    send_email.delay('lyf2000@mail.ru', message)


@shared_task
def send_email(email, message):
    subject = 'NEW BOOK ORDER'
    msg = EmailMultiAlternatives(subject, '', '', [email])
    msg.attach_alternative(message, "text/html")
    msg.send()
