from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from support.models import Ticket, TYPE_STATES
from support.serializers import TicketSerializerAdmin


@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def change_status_ticket_view(request):
    """
                Метод изменения состояния тикета пользователя админом:
        id: 15.(id тикета)
        state_of_request: 0-не решен, 1-решен, 2-заморожен.(Состояния тикета)
    Запрос(с токеном админа):
    {
    "id": 15,
    "state_of_request": 1
    }
    """
    ticket = Ticket.objects.all().get(id=request.data['id'])
    new_state = request.data['state_of_request']
    if ticket:
        if 2 >= new_state >= 0:
            ticket.state_of_request = TYPE_STATES[new_state]
            ticket.save()
        else:
            data = "Не верный статус тикета!"
            return JsonResponse(data, safe=False, status=status.HTTP_400_BAD_REQUEST)
        data = Ticket.objects.all().filter(id=request.data['id'])
        serializer = TicketSerializerAdmin(data, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    else:
        data = "Данного тикета не существует!"
        return JsonResponse(data, safe=False, status=status.HTTP_400_BAD_REQUEST)
