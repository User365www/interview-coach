from django.urls import path
from .views import CandidatesView, CandidateView, HRsView, HRView
# , AuthCheckView)

urlpatterns = [
    path('candidates/', CandidatesView.as_view(), name='candidates-list'),
    path('candidates/<int:id>/', CandidateView.as_view(), name='candidate-detail'),
    path('hrs/', HRsView.as_view(), name='hrs-list'),
    path('hrs/<int:id>/', HRView.as_view(), name='hr-detail'),
    # path('check/', AuthCheckView.as_view(), name='auth-check'),

]