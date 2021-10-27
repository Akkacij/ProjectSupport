from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

# app_name = 'ProjectSupport'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('support/', include(('support.urls', 'support'), namespace='support')),
]