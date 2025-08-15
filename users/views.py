from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Users
from .serializers import HRSerializer, CandidateSerializer, ProfileEditSerializer, MyTokenObtainPairSerializer
from .mixins import ProfileCheckMixin
from django.views import View
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CandidatesView(ProfileCheckMixin, generics.ListAPIView):
    """Список всех кандидатов, отсортированных по пройденным собеседованиям"""
    serializer_class = CandidateSerializer

    def get_queryset(self):
        return Users.objects.filter(type='candidate').order_by('-interview_count_passed')

class CandidateView(ProfileCheckMixin, generics.RetrieveAPIView):
    """Профиль конкретного кандидата"""
    serializer_class = CandidateSerializer
    queryset = Users.objects.filter(type='candidate')

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs['id'])


class HRsView(ProfileCheckMixin, generics.ListAPIView):
    """Список всех HR, отсортированных по проведенным собеседованиям"""
    serializer_class = HRSerializer

    def get_queryset(self):
        return Users.objects.filter(type='HR').order_by('-interview_count_taken')


class HRView(ProfileCheckMixin, generics.RetrieveAPIView):
    """Профиль конкретного HR"""
    serializer_class = HRSerializer
    queryset = Users.objects.filter(type='HR')

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs['id'])


class ProfileEditView(RetrieveUpdateAPIView):
    """Редактирование профиля пользователя"""
    serializer_class = ProfileEditSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Возвращаем профиль текущего пользователя
        return Users.objects.get(user=self.request.user)

    def perform_update(self, serializer):
        # Дополнительные проверки перед сохранением
        instance = serializer.save()
        # Можно добавить логирование изменений
        print(f"Profile updated for user {self.request.user.username}")
