from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from support.serializers import MessageSerializer
from support.models import Message, Ticket, TypeStates
from users.models import User


# The class creates messages for the ticket. Available to all users.
class CreateMessageView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['post']

    def create(self, request):
        request.data['from_user'] = request.user.pk
        ticket = Ticket.objects.all().get(id=request.data['ticket_id'])
        user = User.objects.all().get(id=request.data['from_user'])
        message_count = Message.objects.all().filter(ticket_id=request.data['ticket_id']).count()
        # (Если у тикета уже есть сообщения или сообщение создает админ) и он "не решен"
        if (message_count > 0 or user.is_staff) and ticket.state_of_request == TypeStates.NOT_SOLVED.name:
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        answer = "Message sending is not possible!"
        return JsonResponse(answer, safe=False, status=status.HTTP_400_BAD_REQUEST)
