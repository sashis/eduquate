from functools import reduce

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsObjectOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        assert hasattr(view, 'owner_field'), (
            f"{view.__class__.__name__} class has no 'owner_field' attribute defined."
        )
        if view.owner_field is None:
            return obj == request.user
        try:
            owner = reduce(getattr, view.owner_field.split('__'), obj)
        except AttributeError:
            return False

        return owner == request.user


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS
