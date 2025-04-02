from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),  # User management endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login (Get JWT Token)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]
