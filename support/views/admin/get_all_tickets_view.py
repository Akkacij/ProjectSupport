from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from support.models import Ticket
from support.serializers import TicketSerializerAdmin


# The class returns all existing tickets. Available only to the administrator.
class GetAllTicketsView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializerAdmin
    http_method_names = ['get']
