from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Account

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class RegisterCerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )
    role = serializers.ChoiceField(label="Выберите роль",
                                   choices=((True, "Продавец"),
                                            (False, "Покупатель")),
                                 required=True,
    # validators=[UniqueValidator(queryset=User.objects.all())],
                                   )

    # VENDOR = serializers.CharField(default=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'role']

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."}
    #         )
    #     return attrs


    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
            role=validate_data['role']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user



    def validaterole(self, attrs, Account, request, view):
        is_auth = super().validaterile(request, view)
        user = Account.objects.get(user=request.user)
        if attrs['role'] == True:
            return is_auth
        else:
            False


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']