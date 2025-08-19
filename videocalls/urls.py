# videocalls/urls.py
from django.urls import path
from .views import VideoRoomCreateView

urlpatterns = [
    # Этот путь соответствует окончанию URL-а, на который ругается ошибка.
    path('create-room/', VideoRoomCreateView.as_view(), name='create-video-room'),
]