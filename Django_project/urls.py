# Django_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/auth/', include('users.urls')),
    path('api/candidates/', include('users.urls')),
    path('api/requests/', include('requests.urls')),
    path('api/reports/', include('reports.urls')),
    path('', include('frontend.urls')),

]
