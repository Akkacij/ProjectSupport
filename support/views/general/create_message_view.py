from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from support.serializers import MessageSerializer
from support.models import Message, Ticket, TYPE_STATES
from users.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_message_view(request):
    """
                Метод создания сообщения пользователями(Первое сообщение, как ответ
    на тикет, создает администратор:
        ticket_id: 15.(id тикета)
        text: "текст".(Текст сообщения)
    Запрос(с токеном пользователя):
    {
    "ticket_id": 15,
    "text": "текст"
    }
    """
    request.data['from_user'] = request.user.pk
    ticket = Ticket.objects.all().get(id=request.data['ticket_id'])
    user = User.objects.all().get(id=request.data['from_user'])
    message_count = Message.objects.all().filter(ticket_id=request.data['ticket_id']).count()
    print()
    # Если у тикета уже есть сообщения и он "не решен"
    if (message_count > 0 or user.is_staff) and ticket.state_of_request == str(TYPE_STATES[0]):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    answer = "Отправка сообщения не возможна!"
    return JsonResponse(answer, safe=False, status=status.HTTP_400_BAD_REQUEST)
