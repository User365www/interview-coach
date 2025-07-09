from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from .models import Request
from .serializers import RequestCreateSerializer, RequestAcceptSerializer, RequestSerializer


class RequestCreateView(generics.CreateAPIView):
    """Создание запроса на собеседование"""
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)


class RequestAcceptView(generics.UpdateAPIView):
    """Принятие запроса HR-ом"""
    queryset = Request.objects.filter(status='waiting')
    serializer_class = RequestAcceptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Проверка что пользователь HR
        if not hasattr(request.user, 'profile') or request.user.profile.type != 'HR':
            raise PermissionDenied("Только HR могут принимать запросы")

        instance = self.get_object()
        instance.status = 'accepted'
        instance.hr = request.user
        instance.interview_time = request.data.get('interview_time')
        instance.save() # Укажите ваш URL name


class HRRequestsView(generics.ListAPIView):
    """Список принятых запросов конкретного HR"""
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Проверка что пользователь HR
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.type != 'HR':
            raise PermissionDenied("Только HR могут просматривать принятые запросы")

        return Request.objects.filter(
            hr=self.request.user,
            status='accepted'
        ).order_by('-created_at')


class RequestsWaitingView(generics.ListAPIView):
    """Список ожидающих запросов"""
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Проверка что пользователь HR
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.type != 'HR':
            raise PermissionDenied("Только HR могут просматривать ожидающие запросы")

        return Request.objects.filter(
            status='waiting'
        ).order_by('-created_at')


class UserRequestsView(generics.ListAPIView):
    """Список запросов текущего пользователя"""
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(
            candidate=self.request.user
        ).order_by('-created_at')