from django.urls import include, re_path,path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Mike REST API')




urlpatterns = [
    re_path(r'^$', schema_view),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/', include(("apps.api.urls", "api"), namespace='api')),
]

