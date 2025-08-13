from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Users

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

class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор для регистрации пользователя'''
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user