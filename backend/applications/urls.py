from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationsViewSet

router = DefaultRouter()
router.register("", ApplicationsViewSet, basename="applications")

urlpatterns = [
    path("", include(router.urls)),
]
