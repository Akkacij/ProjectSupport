from django.conf.urls import url
from users.views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView


urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view(), name='user_create'),
    url(r'^obtain_token/$', authenticate_user, name='user_obtain_token'),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view(), name='user_update'),
]
