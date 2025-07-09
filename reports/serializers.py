from rest_framework import serializers
from .models import Report
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ReportCreateSerializer(serializers.ModelSerializer):
    """Создание репорта"""
    class Meta:
        model = Report
        fields = ('description', 'user_reported')

    def create(self, validated_data):
        user = self.context['request'].user  # Исправил 'report' на 'request'
        return Report.objects.create(
            user_reporting=user,
            user_reported=validated_data['user_reported'],
            description=validated_data['description']
        )


class ReportAcceptSerializer(serializers.ModelSerializer):
    """Обработка репорта админом"""
    interview_time = serializers.DateTimeField(required=True)
    class Meta:
        model = Report
        fields = ('id', 'status')
        read_only_fields = ('id',)


class UserReportsSerializer(serializers.ModelSerializer):
    """Список репортов пользователя"""
    class Meta:
        model = Report
        fields = ('id', 'status', 'description', 'user_reported', 'created_at')


class ReportSerializer(serializers.ModelSerializer):
    """Список ожидающих репортов"""
    user_reporting = UserSerializer(read_only=True)
    user_reported = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = '__all__'