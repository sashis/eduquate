from rest_framework.viewsets import ModelViewSet


class EduquateViewSet(ModelViewSet):
    owner_field = None
    permission_action_classes = dict()
    serializer_action_class = dict()

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
