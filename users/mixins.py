from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Users  # Импортируйте вашу модель профиля

User = get_user_model()


class ProfileCheckMixin:
    """Mixin для проверки и создания профиля пользователя"""

    def __init__(self):
        pass

    def dispatch(self, request, *args, **kwargs):
        # Проверяем наличие профиля
        try:
            request.user.profile  # Или request.user.users, в зависимости от вашей related_name
        except (ObjectDoesNotExist, AttributeError):
            # Создаем профиль, если его нет
            Users.objects.create(user=request.user)

        return super().dispatch(request, *args, **kwargs)