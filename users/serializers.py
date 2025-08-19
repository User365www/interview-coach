from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Users, STATUS_CHOICES
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    # ---- ПОЛЯ ИЗ ПРОФИЛЯ ----
    # Мы объявляем их здесь вручную, т.к. они не принадлежат основной модели `User`
    name = serializers.CharField(write_only=True, required=True, max_length=100)
    type = serializers.ChoiceField(choices=STATUS_CHOICES, write_only=True)
    description = serializers.CharField(write_only=True, required=False, allow_blank=True)

    # ---- ПОЛЯ ДЛЯ СОЗДАНИЯ User ----
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User  # Основная модель все еще User
        fields = ['username', 'password', 'password2', 'name', 'type', 'description']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Создаем основного пользователя (User)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        # Создаем связанный с ним профиль (Users)
        Users.objects.create(
            user=user,
            name=validated_data['name'],
            type=validated_data['type'],
            description=validated_data.get('description', '')  # .get() для безопасности
        )
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['type'] = user.profile.type
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

