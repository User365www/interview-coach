from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Report
from .serializers import ReportCreateSerializer, ReportAcceptSerializer, ReportSerializer
from users.mixins import ProfileCheckMixin


class ReportCreateView(ProfileCheckMixin, generics.CreateAPIView):
    """Создание репорта"""
    queryset = Report.objects.all()
    serializer_class = ReportCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_reporting=self.request.user)



class ReportAcceptView(ProfileCheckMixin, generics.UpdateAPIView):
    """Принятие репорта админом"""
    queryset = Report.objects.filter(status='waiting')
    serializer_class = ReportAcceptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Проверка что пользователь admin
        if not hasattr(request.user, 'profile') or request.user.profile.type != 'admin':
            raise PermissionDenied("Только админы могут обрабатывать репорты")

        instance = self.get_object()
        instance.status = 'done'
        instance.admin = request.user
        instance.save()
        return Response({'status': 'done'})


class adminReportsView(ProfileCheckMixin, generics.ListAPIView):
    """Список обработанных репортов конкретного админа"""
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.type != 'admin':
            raise PermissionDenied("Только админы могут просматривать обработанные репорты")

        return Report.objects.filter(
            admin=self.request.user,
            status='done'
        ).order_by('-created_at')


class ReportsWaitingView(ProfileCheckMixin, generics.ListAPIView):
    """Список ожидающих репортов"""
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Проверка что пользователь HR
        if not hasattr(self.request.user, 'profile') or self.request.user.profile.type != 'admin':
            raise PermissionDenied("Только админы могут просматривать ожидающие репорты")

        return Report.objects.filter(
            status='waiting'
        ).order_by('-created_at')


class UserReportsView(ProfileCheckMixin, generics.ListAPIView):
    """Список репортов текущего пользователя"""
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Report.objects.filter(
            user_reporting=self.request.user
        ).order_by('-created_at')