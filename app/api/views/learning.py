from rest_framework import permissions

from learning.models import CourseSubscription
from ..serializers import CourseSubscriptionSerializer
from ..viewsets import EduquateViewSet


class CourseSubscriptionViewSet(EduquateViewSet):
    owner = 'student'
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(student=self.request.user)
