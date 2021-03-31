from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import User
from ..permissions import ReadOnly
from ..serializers import AccountSerializer, AccountPersonalSerializer
from ..viewsets import EduquateViewSet


class AccountViewSet(EduquateViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    serializer_action_class = {
        'me': AccountPersonalSerializer
    }
    permission_classes = [permissions.IsAdminUser | ReadOnly]
    permission_action_classes = {
        'list': [permissions.IsAdminUser],
        'create': [~permissions.IsAuthenticated],
        'me': [permissions.IsAuthenticated]
    }

    @action(detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @me.mapping.patch
    def update_me(self, request):
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @me.mapping.delete
    def destroy_me(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
