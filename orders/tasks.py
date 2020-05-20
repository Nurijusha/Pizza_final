from celery import task
from django.core.mail import send_mail
from .models import Order
import os
import myEnvVal


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = "Заказ пиццы {}".format(order.id)
    message = "Здравствуйте, {}! \n\nВаш заказ принят.\
               \nНомер Вашего заказа {}.".format(order.first_name, order.id)
    myEnvVal.setVar()
    email_from = os.environ.get('EMAIL_HOST_USER')
    mail_sent = send_mail(subject, message,
                          email_from,
                          [order.email],
                          fail_silently=False)
    return mail_sent
