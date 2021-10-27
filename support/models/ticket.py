from django.db import models
from django.utils import timezone

from users.models import User


# Состояния тикета
TYPE_STATES = [
    ('Не решён', 'не решён'),
    ('Решён', 'решён'),
    ('Заморожен', 'заморожен'),
]


class Ticket(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket')
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    date_of_request = models.DateTimeField(default=timezone.now)
    state_of_request = models.CharField(default=TYPE_STATES[0], choices=TYPE_STATES, max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'
