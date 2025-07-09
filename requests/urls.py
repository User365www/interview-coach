from django.urls import path
from .views import RequestCreateView, RequestAcceptView, HRRequestsView, RequestsWaitingView, UserRequestsView

urlpatterns = [
    path('create-request/', RequestCreateView.as_view(), name='request-create'),
    path('accept-request/<int:pk>', RequestAcceptView.as_view(), name='request-accept'),
    path('my-HR-requests/', HRRequestsView.as_view(), name='hr-requests'),
    path('waiting-requests/', RequestsWaitingView.as_view(), name='requests-waiting'),
    path('my-candidate-requests/', UserRequestsView.as_view(), name='user-requests'),
]