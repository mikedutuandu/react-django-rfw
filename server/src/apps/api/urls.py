
from django.urls import include, re_path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from .views import (
    UserCreateAPIView,
    UserListAPIView,
UserDeleteAPIView
    )

urlpatterns = [
    re_path(r'^auth/token/$', obtain_jwt_token, name='get-jwt-token'),

    re_path(r'^register/$', UserCreateAPIView.as_view(), name='register'),

    re_path(r'^users/$', UserListAPIView.as_view(), name='list'),
    re_path(r'^users/(?P<pk>\d+)$', UserDeleteAPIView.as_view(), name='delete'),

]