from rest_framework import viewsets, permissions
from .models import Application
from .serializers import ApplicationsSerializer
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter


@extend_schema(
    request=ApplicationsSerializer,  # Specify the request serializer
    responses={200: ApplicationsSerializer},  # Specify the response serializer
    parameters=[
        OpenApiParameter("pk", OpenApiTypes.INT, OpenApiParameter.PATH, description="Primary key of the application"),
    ],
    description="Custom description for the ApplicationsViewSet",
    tags=["applications"],  # Add tags to categorize your API endpoints
)
class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated]
