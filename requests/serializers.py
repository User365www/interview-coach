from rest_framework import serializers
from .models import Request
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RequestCreateSerializer(serializers.ModelSerializer):
    """Создание запроса на собеседование"""
    class Meta:
        model = Request
        fields = ('description',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Request.objects.create(
            candidate=user,
            description=validated_data['description']
        )


class RequestAcceptSerializer(serializers.ModelSerializer):
    """Принятие запроса HR-ом"""
    interview_time = serializers.DateTimeField(required=True)
    class Meta:
        model = Request
        fields = ('id', 'status', 'interview_time')
        read_only_fields = ('id',)


class UserRequestsSerializer(serializers.ModelSerializer):
    """Список запросов пользователя"""
    class Meta:
        model = Request
        fields = ('id', 'status', 'interview_time', 'hr', 'created_at')


class RequestSerializer(serializers.ModelSerializer):
    """Список ожидающих запросов"""
    candidate = UserSerializer(read_only=True)
    hr = UserSerializer(read_only=True)

    class Meta:
        model = Request
        fields = '__all__'