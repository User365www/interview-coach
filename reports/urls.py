from django.urls import path
from .views import ReportCreateView, ReportAcceptView, adminReportsView, ReportsWaitingView, UserReportsView

urlpatterns = [
    path('create-report/', ReportCreateView.as_view(), name='request-create'),
    path('accept-report/<int:pk>', ReportAcceptView.as_view(), name='request-accept'),
    path('my-admin-reports/', adminReportsView.as_view(), name='hr-requests'),
    path('waiting-reports/', ReportsWaitingView.as_view(), name='requests-waiting'),
    path('my-user-reports/', UserReportsView.as_view(), name='user-requests'),
]