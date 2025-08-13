from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('login', index),
    path('profile', index),
    path('logout', index),
    path('register', index),
    path('reports', index),
    path('candidates', index),
    path('hr-list', index),
]