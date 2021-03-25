from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from accounts.models import User
from courses.models import Course
from .viewsets import EduquateViewSet
from .permissions import IsObjectOwner, ReadOnly
from .serializers import AccountSerializer, AccountDetailSerializer, CourseSerializer


class AccountViewSet(EduquateViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [ReadOnly|IsObjectOwner]
    permission_action_classes = {
        'list': [permissions.IsAdminUser],
        'create': [~permissions.IsAuthenticated],
    }

    @action(detail=False, serializer_class=AccountDetailSerializer)
    def me(self, request, *args, **kwargs):
        serialized_user = self.get_serializer(request.user)
        print(serialized_user.context)
        return Response(serialized_user.data)


class CourseViewSet(EduquateViewSet):
    queryset = Course.objects.all()
    owner_field = 'tutor'
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TokenViewSet(TokenObtainPairView, viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @action(detail=False, methods=['post'], serializer_class=TokenRefreshSerializer)
    def refresh(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
