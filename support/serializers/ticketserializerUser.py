from rest_framework import serializers
from support.models import Ticket


class TicketSerializerUser(serializers.ModelSerializer):

    class Meta():
        model = Ticket
        fields = ['id', 'from_user', 'title', 'description', 'state_of_request']
