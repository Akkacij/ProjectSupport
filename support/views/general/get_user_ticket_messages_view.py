from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from support.models import Message, Ticket
from users.models import User
from support.serializers import MessageSerializer


# The class returns all messages for the given ticket. Available to all users.
class GetUserTicketMessagesView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get']

    def list(self, request):
        user_id = request.user.pk
        ticket_id = request.data['ticket_id']
        if ((User.objects.all().get(id=user_id).is_staff and Ticket.objects.all().filter(id=ticket_id)) or
                (Ticket.objects.all().filter(from_user=user_id, id=ticket_id))):
            data = Message.objects.all().filter(ticket_id=ticket_id)
            serializer = MessageSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            data = "This ticket does not exist, or the user does not have access to this ticket!"
            return JsonResponse(data, safe=False, status=status.HTTP_400_BAD_REQUEST)
