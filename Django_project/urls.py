# Django_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.views import MyTokenObtainPairView

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    # API endpoints
    path('api/users/', include('users.urls')),
    path('api/requests/', include('requests.urls')),
    path('api/reports/', include('reports.urls')),
    path('', include('frontend.urls')),
]
