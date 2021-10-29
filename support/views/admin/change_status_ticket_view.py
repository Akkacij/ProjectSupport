from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser

from support.models import Ticket, TypeStates
from support.serializers import TicketSerializerAdmin



# The class changes the status of the ticket. Available only to the administrator.
class ChangeStatusTicketView(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializerAdmin
    http_method_names = ['get']

    def list(self, request):
        new_state = request.data['state_of_request']
        if Ticket.objects.all().filter(id=request.data['id']).count() == 1:
            ticket = Ticket.objects.all().get(id=request.data['id'])
            if 2 >= new_state >= 0:
                ticket.state_of_request = TypeStates(new_state).name
                ticket.save()
            else:
                data = "Invalid ticket status!"
                return JsonResponse(data, safe=False, status=status.HTTP_400_BAD_REQUEST)
            data = Ticket.objects.all().filter(id=request.data['id'])
            serializer = TicketSerializerAdmin(data, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            data = "Received ticket id does not exist!"
            return JsonResponse(data, safe=False, status=status.HTTP_400_BAD_REQUEST)
