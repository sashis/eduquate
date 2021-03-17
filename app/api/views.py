from rest_framework import viewsets, permissions

from accounts.models import User
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
