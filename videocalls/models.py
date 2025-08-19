import uuid
from django.db import models
from django.conf import settings


class VideoRoom(models.Model):
    # Используем UUID для уникальных и непредсказуемых ссылок
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # HR, который создал комнату
    hr = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_rooms'
    )

    # Название (для удобства)
    name = models.CharField(max_length=100, verbose_name="Название комнаты")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комната {self.name} (HR: {self.hr.username})"