from django.urls import path
from .views import CandidatesView, CandidateView, HRsView, HRView, ProfileEditView, RegisterView


urlpatterns = [
    path('candidates/', CandidatesView.as_view(), name='candidates-list'),
    path('candidates/<int:id>/', CandidateView.as_view(), name='candidate-detail'),
    path('hrs/', HRsView.as_view(), name='hrs-list'),
    path('hrs/<int:id>/', HRView.as_view(), name='hr-detail'),
    path('profile/', ProfileEditView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]