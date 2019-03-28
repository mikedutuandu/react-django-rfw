from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
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
User = get_user_model()


from .serializers import (
    UserCreateSerializer,
    UserDetailSerializer
    )





#view----------------



class UserListAPIView(ListAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserDeleteAPIView(DestroyAPIView):
    # serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


