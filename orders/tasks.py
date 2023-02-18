from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа. 
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ - {}'.format(order_id)
    message = 'Уважаемый {},\n\nВы успешно оформили заказ.\
                Номер Вашего заказа {}.'.format(order.first_name,
                                                order.id)
    mail_sent = send_mail(subject,
                          message,
                          'python_inter@mail.ru',
                          [order.email])
    return mail_sent
