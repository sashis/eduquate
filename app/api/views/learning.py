from rest_framework import permissions

from learning.models import CourseSubscription
from ..serializers import CourseSubscriptionSerializer
from ..viewsets import EduquateViewSet


class CourseSubscriptionViewSet(EduquateViewSet):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [permissions.AllowAny]