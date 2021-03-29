from rest_framework import permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from courses.models import Course, Lesson
from ..permissions import IsTutor, IsObjectOwner, ReadOnly
from ..serializers import CourseSerializer, CourseDetailSerializer
from ..viewsets import EduquateViewSet


class CourseViewSet(EduquateViewSet):
    queryset = Course.objects.with_counts('students', 'lessons')
    owner_field = 'tutor'
    serializer_class = CourseSerializer
    permission_classes = [ReadOnly | IsObjectOwner]
    permission_action_classes = {
        'create': [IsTutor],
        'subscribe': [permissions.IsAuthenticated, ~IsObjectOwner]
    }

    @action(detail=True, methods=['post'])
    def subscribe(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user.id)
        subscription = request.user.subscriptions.get(course=course)
        serializer = self.get_serializer(subscription)
        return Response(serializer.data)
