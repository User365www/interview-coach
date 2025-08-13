from django.urls import path
from .views import CandidatesView, CandidateView, HRsView, HRView, RegisterView


urlpatterns = [
    path('candidates/', CandidatesView.as_view(), name='candidates-list'),
    path('candidates/<int:id>/', CandidateView.as_view(), name='candidate-detail'),
    path('hrs/', HRsView.as_view(), name='hrs-list'),
    path('hrs/<int:id>/', HRView.as_view(), name='hr-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]