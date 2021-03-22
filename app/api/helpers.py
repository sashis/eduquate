from rest_framework.viewsets import ModelViewSet


class EduquateViewSet(ModelViewSet):
    permission_action_classes = dict()
    serializer_action_class = dict()

    def get_serializer_class(self):
        try:
            return self.serializer_action_class[self.action]
        except KeyError:
            return super().get_serializer_class()

    def get_permissions(self):
        try:
            self.permission_classes = self.permission_action_classes[self.action]
        except KeyError:
            pass
        return super().get_permissions()