from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    # email = EmailField(label='Email Address')
    # email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            # 'first_name',
            # 'last_name',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }


    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        # first_name = validated_data['first_name']
        # last_name = validated_data['last_name']
        password = validated_data['password']
        user_obj = User(
            username=username,
            # first_name=first_name,
            # last_name=last_name,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

