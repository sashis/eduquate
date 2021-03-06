from rest_framework import permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from courses.models import Course, Lesson
from ..permissions import IsTutor, IsObjectOwner, ReadOnly
from ..serializers import CourseListSerializer, CourseSerializer
from ..viewsets import EduquateViewSet


class CourseViewSet(EduquateViewSet):
    owner_field = 'tutor'
    queryset = Course.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['pk', 'num_students']
    ordering = ['pk']
    queryset_action = {
        'list': Course.objects.with_counts('students', 'lessons').select_related('tutor').order_by('-num_students')
    }
    serializer_class = CourseSerializer
    serializer_action_class = {
        'list': CourseListSerializer
    }
    permission_classes = [ReadOnly | IsObjectOwner]
    permission_action_classes = {
        'create': [IsTutor],
        'subscribe': [permissions.IsAuthenticated, ~IsObjectOwner]
    }
