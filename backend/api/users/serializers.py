from rest_framework import serializers
from .models import User
from api.tickets.serializers import TicketSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'tickets']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise AuthenticationFailed('잘못된 자격 증명입니다.')
        return user