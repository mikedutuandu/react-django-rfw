from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,

    )


from .serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer
    )

from apps.api.models import User
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework_json_api.pagination import JsonApiPageNumberPagination
from django.conf import settings


#view----------------


class PaginationAPIView(APIView):
    '''
    APIView with pagination
    '''

    pagination_class = settings.REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS']

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

class DriverList(PaginationAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    parser_classes = (FormParser, MultiPartParser)
    pagination_class = JsonApiPageNumberPagination


    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        queryset = User.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserListSerializer(queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

