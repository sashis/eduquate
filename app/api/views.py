from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from accounts.models import User
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class TokenViewSet(TokenObtainPairView, viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @action(detail=False, methods=['post'], serializer_class=TokenRefreshSerializer)
    def refresh(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
