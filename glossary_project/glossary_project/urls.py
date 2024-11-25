from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('glossary.urls')),  # подключение маршрутов из приложения `glossary`
]
