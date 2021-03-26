from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenViewSet(TokenObtainPairView, ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @action(detail=False, methods=['post'], serializer_class=TokenRefreshSerializer)
    def refresh(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
