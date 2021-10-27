from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from support.models import Ticket
from support.serializers import TicketSerializerUser


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_user_tickets_view(request):
    """
                Метод получения всех своих тикетов пользователем:
    Запрос(с токеном пользователя):пустой
    """
    user_id = request.user.pk
    data = Ticket.objects.all().filter(from_user=user_id)
    serializer = TicketSerializerUser(data, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
