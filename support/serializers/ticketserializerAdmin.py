from rest_framework import serializers
from support.models import Ticket


class TicketSerializerAdmin(serializers.ModelSerializer):

    class Meta():
        model = Ticket
        fields = '__all__'
