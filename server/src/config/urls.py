from django.urls import include, re_path,path
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    re_path(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/', include(("apps.api.urls", "api"), namespace='api')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)