from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import obtain_jwt_token






urlpatterns = [
    url(r'^api/users/', include(("apps.api.urls","api"), namespace='users-api')),

    url(r'^api/auth/token/', obtain_jwt_token),
]