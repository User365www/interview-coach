from django.urls import path
from .views import RequestCreateView, RequestAcceptView, HRRequestsView, RequestsWaitingView

urlpatterns = [
    path('create/', RequestCreateView.as_view(), name='request-create'),
    path('accept/<int:pk>', RequestAcceptView.as_view(), name='request-accept'),
    path('my-requests/', HRRequestsView.as_view(), name='hr-requests'),
    path('waiting/', RequestsWaitingView.as_view(), name='requests-waiting'),
]