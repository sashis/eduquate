from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from accounts.models import User
from courses.models import Course
from .helpers import EduquateViewSet
from .serializers import AccountSerializer, CourseSerializer


class AccountViewSet(EduquateViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_action_classes = {
        'list': [permissions.IsAdminUser],
        'create': [~permissions.IsAuthenticated],
        'me': [permissions.IsAuthenticated]
    }

    @action(detail=False, methods=['get', 'put', 'patch', 'delete'])
    def me(self, request, *args, **kwargs):
        serialized_user = self.get_serializer(request.user)
        return Response(serialized_user.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TokenViewSet(TokenObtainPairView, viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @action(detail=False, methods=['post'], serializer_class=TokenRefreshSerializer)
    def refresh(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
