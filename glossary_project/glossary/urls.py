from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProjectViewSet, TermViewSet, RegisterView, TermsByReferrerView

# Основной роутер для проектов
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

# Вложенный роутер для терминов, привязанных к проектам
projects_router = NestedDefaultRouter(router, r'projects', lookup='project')
projects_router.register(r'terms', TermViewSet, basename='project-terms')

urlpatterns = [
    path('', include(router.urls)),                 # маршруты для проектов
    path('', include(projects_router.urls)),        # вложенные маршруты для терминов в рамках проектов
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # получение токенов
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # обновление токенов
    path('register/', RegisterView.as_view(), name='register'),                # регистрация
    path('terms-by-referrer/', TermsByReferrerView.as_view(), name='terms-by-referrer'),  # получение терминов по домену
]
