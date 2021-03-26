from rest_framework import viewsets, permissions
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
    permission_classes = [ReadOnly | IsObjectOwner]
    permission_action_classes = {
        'list': [permissions.IsAdminUser],
        'create': [~permissions.IsAuthenticated],
    }

    @action(detail=False, serializer_class=AccountDetailSerializer)
    def me(self, request, *args, **kwargs):
        serialized_user = self.get_serializer(request.user)
        return Response(serialized_user.data)


class CourseViewSet(EduquateViewSet):
    queryset = Course.objects.prefetch_related('students')
    owner_field = 'tutor'
    serializer_class = CourseSerializer
    permission_classes = [ReadOnly]

    @action(detail=True, methods=['post'])
    def subscribe(self, request, *args, **kwargs):
        course = self.get_object()
        subscription = self.get_serializer(course, request.user)
        return Response(subscription.data)


class TokenViewSet(TokenObtainPairView, viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @action(detail=False, methods=['post'], serializer_class=TokenRefreshSerializer)
    def refresh(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
