from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from support.models import Ticket
from support.serializers import TicketSerializerUser


# The class creates a ticket. Available to all users.
class CreateTicketView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializerUser
    http_method_names = ['post']

    def create(self, request):
        request.data['from_user'] = request.user.pk
        serializer = TicketSerializerUser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
