from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig

from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    ProductViewSet,
    UserViewSet,
)

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    # users
    path("", include(router.urls)),
    # token
    path(
        "login/",
        CustomTokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "token/refresh/",
        CustomTokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
