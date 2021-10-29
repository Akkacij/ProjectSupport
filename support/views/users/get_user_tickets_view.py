from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from support.models import Ticket
from support.serializers import TicketSerializerUser


# The class returns all user tickets. Available to all users.
class GetUserTicketsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializerUser
    http_method_names = ['get']

    def list(self, request):
        user_id = request.user.pk
        data = Ticket.objects.all().filter(from_user=user_id)
        serializer = TicketSerializerUser(data, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
