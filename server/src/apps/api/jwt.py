
from .serializers import (
    UserDetailSerializer
    )

from rest_framework_jwt.settings import api_settings

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        # 'user': UserDetailSerializer(user, context={'request': request}).data
    }

def create_jwt_token_from_user(user):

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return token
