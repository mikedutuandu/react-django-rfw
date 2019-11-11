
from django.urls import include, re_path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, re_path, path


from .views import (DriverList)

urlpatterns = [
    re_path(r'^auth/token$', obtain_jwt_token, name='get-jwt-token'),

    re_path(r'^drivers$', DriverList.as_view(), name='driver_list'),


]


