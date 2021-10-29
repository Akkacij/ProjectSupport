from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from support.views import GetAllTicketsView, GetNotResolvedTicketsView, ChangeStatusTicketView, \
    CreateMessageView, GetUserTicketMessagesView, CreateTicketView, GetUserTicketsView

router = routers.SimpleRouter()
router.register(r'getticketall', GetAllTicketsView)
router.register(r'getnotresolvedtickets', GetNotResolvedTicketsView)
router.register(r'changestatusticket', ChangeStatusTicketView)
router.register(r'createmessage', CreateMessageView)
router.register(r'getuserticketmessages', GetUserTicketMessagesView)
router.register(r'createticket', CreateTicketView)
router.register(r'getuserticket', GetUserTicketsView)


urlpatterns = [
    url('', include(router.urls)),
]
