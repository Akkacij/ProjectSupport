from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from support.models import Ticket
from support.serializers import TicketSerializerAdmin


@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def get_not_resolved_tickets_view(request):
    """
                Метод получения всех 'не решённых' тикетов пользователей админами:
    Запрос(с токеном админа): пустой
    """
    data = Ticket.objects.all().filter(state_of_request=('Не решён', 'не решён'))
    serializer = TicketSerializerAdmin(data, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
