from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class BaseEduquateViewSet(GenericViewSet):
    owner = None
    queryset_action = dict()
    serializer_action_class = dict()
    permission_action_classes = dict()

    def get_queryset(self):
        return self.queryset_action.get(
            self.action,
            self.queryset
        )

    def get_serializer_class(self):
        return self.serializer_action_class.get(
            self.action,
            self.serializer_class
        )

    def get_permissions(self):
        permission_classes = self.permission_action_classes.get(
            self.action,
            self.permission_classes
        )
        return [permission() for permission in permission_classes]


class EduquateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseEduquateViewSet
):
    pass


class NoListEduquateViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseEduquateViewSet
):
    pass
