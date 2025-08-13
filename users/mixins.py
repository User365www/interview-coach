from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ProfileCheckMixin:
    """Mixin для проверки и создания профиля пользователя"""

    def __init__(self):
        pass

    def dispatch(self, request, *args, **kwargs):
        # Аутентификация через JWT
        try:
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(request.auth)
            user = jwt_auth.get_user(validated_token)
            request.user = user
        except Exception:
            raise AuthenticationFailed('Неверные учетные данные')

        # Проверяем наличие профиля
        try:
            request.user.profile
        except (ObjectDoesNotExist, AttributeError):
            # Создаем профиль, если его нет
            Users.objects.create(user=request.user)

        return super().dispatch(request, *args, **kwargs)