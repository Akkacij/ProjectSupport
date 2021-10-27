from django.db import models
from django.utils import timezone

from support.models import Ticket
from users.models import User


class Message(models.Model):
    # Хранит id USERа который отправил сообщение
    from_user = models.IntegerField()
    # Хранит id-TICKET которому принадлежит сообщение
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='message')
    # Текст сообщения
    text = models.TextField(max_length=1000)
    # Дата создания сообщения
    date_of_message = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (str(self.ticket_id.id)
                + ":"
                + "Сообщение"
                + ":"
                + self.text[0:30]
                + ":"
                + str(User.objects.all().get(id=self.from_user)))

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
