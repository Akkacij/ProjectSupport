from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from support.models import Ticket, TypeStates
from support.serializers import TicketSerializerAdmin


# The class returns all unresolved tickets. Available only to the administrator.
class GetNotResolvedTicketsView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Ticket.objects.all().filter(state_of_request=TypeStates.NOT_SOLVED.name)
    serializer_class = TicketSerializerAdmin
    http_method_names = ['get']
