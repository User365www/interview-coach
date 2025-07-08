from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Request
from .serializers import RequestCreateSerializer, RequestAcceptSerializer, RequestSerializer

User = get_user_model()

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
        instance = self.get_object()
        instance.status = 'accepted'
        instance.hr = request.user
        instance.save()
        return Response({'status': 'request accepted'})

class HRRequestsView(generics.ListAPIView):
    """Список принятых запросов конкретного HR"""
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(
            hr=self.request.user,
            status='accepted'
        ).order_by('-created_at')

class RequestsWaitingView(generics.ListAPIView):
    """Список ожидающих запросов"""
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(
            status='waiting'
        ).order_by('-created_at')