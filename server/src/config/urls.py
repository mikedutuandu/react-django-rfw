from django.urls import include, re_path,path




urlpatterns = [

    re_path(r'^api/', include(("apps.api.urls", "api"), namespace='api')),
]

