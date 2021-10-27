from django.conf.urls import url
from support.views import create_ticket_view, get_user_tickets_view, get_all_tickets_view, \
    get_not_resolved_tickets_view, get_user_ticket_messages_view, create_message_view, change_status_ticket_view

urlpatterns = [
    url(r'^createticket/$', create_ticket_view, name='create_ticket'),
    url(r'^getuserticket/$', get_user_tickets_view, name='get_user_ticket'),
    url(r'^getticketall/$', get_all_tickets_view, name='get_all_tickets'),
    url(r'^getnotresolvedtickets/$', get_not_resolved_tickets_view, name='get_not_resolved_tickets'),
    url(r'^getuserticketmessages/$', get_user_ticket_messages_view, name='get_user_ticket_messages'),
    url(r'^createmessage/$', create_message_view, name='create_message'),
    url(r'^changestatusticket/$', change_status_ticket_view, name='change_status_ticket'),
]
