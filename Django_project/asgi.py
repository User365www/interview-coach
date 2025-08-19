import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack # Понадобится для аутентификации в WebSocket
import videocalls.routing # <-- Импортируем нашу новую "карту" маршрутов

# Указываем путь к настройкам Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_project.settings')

# --- ЭТОТ КОД ---
# заменяет стандартную строку `application = get_asgi_application()`

# application - это главный маршрутизатор, который смотрит на тип протокола
application = ProtocolTypeRouter({

  # Если это обычный HTTP-запрос (зайти на страницу, получить API),
  # то используем стандартный обработчик Django.
  "http": get_asgi_application(),

  # Если это WebSocket-запрос (ws://...),
  # то используем наш собственный маршрутизатор.
  "websocket": AuthMiddlewareStack( # AuthMiddlewareStack добавляет поддержку сессий и пользователей
        URLRouter(
            # Django посмотрит в этот список...
            videocalls.routing.websocket_urlpatterns
            # ... и найдет там подходящий маршрут.
        )
    ),
})