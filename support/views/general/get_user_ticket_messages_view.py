from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from support.models import Message, Ticket
from users.models import User
from support.serializers import MessageSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_user_ticket_messages_view(request):
    """
                Метод получения всех сообщений своего конкретного тикета пользователем или всех сообщений
    любого тикета админами:
        ticket_id: 15.(id тикета)
    Запрос(с токеном пользователя):
    {
    "ticket_id": 14
    }
    """
    user_id = request.user.pk
    ticket_id = request.data['ticket_id']
    if ((User.objects.all().get(id=user_id).is_staff and Ticket.objects.all().filter(id=ticket_id)) or
            (Ticket.objects.all().filter(from_user=user_id, id=ticket_id))):
        data = Message.objects.all().filter(ticket_id=ticket_id)
        serializer = MessageSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    else:
        data = "Данного тикета не существует, либо пользователь не имеет доступа к данному тикету"
        return JsonResponse(data, safe=False, status=status.HTTP_400_BAD_REQUEST)
