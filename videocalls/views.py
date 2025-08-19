# videocalls/views.py

from rest_framework import generics, permissions
# Убедитесь, что импортировали вашу модель и сериализатор
from .models import VideoRoom
from .serializers import VideoRoomSerializer

class VideoRoomCreateView(generics.CreateAPIView):
    queryset = VideoRoom.objects.all()
    serializer_class = VideoRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    # --- ДОБАВЬТЕ ЭТОТ МЕТОД ---
    # Этот метод вызывается прямо перед сохранением нового объекта.
    # Он позволяет нам добавить данные, которых нет в запросе.
    def perform_create(self, serializer):
        # Мы говорим: "Сохрани объект, но в поле `hr` запиши текущего пользователя"
        serializer.save(hr=self.request.user)