from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class HRSerializer(serializers.ModelSerializer):
    '''Лидерборд HR'''
    class Meta:
        model = Users
        fields = 'name', 'description', 'interview_count_taken'

class CandidateSerializer(serializers.ModelSerializer):
    '''Лидерборд кандидатов'''
    class Meta:
        model = Users
        fields = 'name', 'description', 'interview_count_passed', 'positive_results', 'negative_results'

class ProfileEditSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования профиля"""
    class Meta:
        model = Users
        fields = ['name', 'description', 'interview_count_passed', 'positive_results', 'negative_results', 'interview_count_taken', 'type']
        extra_kwargs = {
            'type': {'read_only': True}  # Запрещаем менять тип пользователя
        }

