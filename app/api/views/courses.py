from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from courses.models import Course, Lesson
from ..serializers import CourseSerializer
from ..viewsets import EduquateViewSet


class CourseViewSet(EduquateViewSet):
    queryset = Course.objects.with_counts('students', 'lessons')
    owner_field = 'tutor'
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def subscribe(self, request, *args, **kwargs):
        course = self.get_object()
        subscription = self.get_serializer(course, request.user)
        return Response(subscription.data)
