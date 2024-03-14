from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134326ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134326", Testconnectors134326ViewSet, basename="testconnectors134326"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
