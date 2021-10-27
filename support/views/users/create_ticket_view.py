from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from support.serializers import TicketSerializerUser


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_ticket_view(request):
    """
                Метод создания тикета пользователями:
        title: "Тикет".(Краткое описание тикета)
        description: "Описание проблемы".(Описание тикета)
    Запрос(с токеном пользователя):
    {
    "title": "Тикет",
    "description": "Описание проблемы"
    }
    """
    request.data['from_user'] = request.user.pk
    serializer = TicketSerializerUser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
