from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import User
from ..permissions import ReadOnly, IsObjectOwner
from ..serializers import AccountSerializer, AccountDetailSerializer
from ..viewsets import EduquateViewSet


class AccountViewSet(EduquateViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [ReadOnly | IsObjectOwner]
    permission_action_classes = {
        'list': [permissions.IsAdminUser],
        'create': [~permissions.IsAuthenticated],
        'me': [permissions.IsAuthenticated]
    }

    @action(detail=False, serializer_class=AccountDetailSerializer)
    def me(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)
