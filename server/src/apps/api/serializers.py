from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

from apps.api.models import User



class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
        ]


class UserListSerializer(ModelSerializer):
    avatar = SerializerMethodField()
    avatar_thumb = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'driver_license',
            'license_plate',
            'vehicle_make',
            'vehicle_model',
            'vehicle_color',
            'vehicle_year',
            'avatar',
            'avatar_thumb'
        ]

    def get_avatar(self, obj):
        try:
            avatar = obj.avatar.url
        except:
            avatar = None
        return avatar
    def get_avatar_thumb(self, obj):
        try:
            avatar_thumb = obj.avatar_thumb.url
        except:
            avatar_thumb = None
        return avatar_thumb

class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'driver_license',
            'license_plate',
            'vehicle_make',
            'vehicle_model',
            'vehicle_color',
            'vehicle_year',
            'working_days',
            'avatar',

        ]
        extra_kwargs = {"password":{"write_only": True}}


    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        data['username'] = data['email']
        return data

    def create(self, validated_data):
        user_obj = super().create(validated_data)
        password = validated_data['password']
        user_obj.set_password(password)
        user_obj.is_driver = True
        user_obj.save()
        return user_obj

