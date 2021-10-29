from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from users.views import CreateOrUpdateUser, AuthenticateUser

router = routers.SimpleRouter()
router.register(r'createorupdate', CreateOrUpdateUser)
router.register(r'obtain_token', AuthenticateUser)

urlpatterns = [
    url('', include(router.urls)),
]
