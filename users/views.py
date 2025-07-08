from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Users
from .serializers import HRSerializer, CandidateSerializer


class CandidatesView(generics.ListAPIView):
    """Список всех кандидатов, отсортированных по пройденным собеседованиям"""
    serializer_class = CandidateSerializer

    def get_queryset(self):
        return Users.objects.filter(type='candidate').order_by('-interview_count_passed')


class CandidateView(generics.RetrieveAPIView):
    """Профиль конкретного кандидата"""
    serializer_class = CandidateSerializer
    queryset = Users.objects.filter(type='candidate')

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs['id'])


class HRsView(generics.ListAPIView):
    """Список всех HR, отсортированных по проведенным собеседованиям"""
    serializer_class = HRSerializer

    def get_queryset(self):
        return Users.objects.filter(type='HR').order_by('-interview_count_taken')


class HRView(generics.RetrieveAPIView):
    """Профиль конкретного HR"""
    serializer_class = HRSerializer
    queryset = Users.objects.filter(type='HR')

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs['id'])