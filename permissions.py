from rest_framework.permissions import BasePermission


class IsAnonymoused(BasePermission):
    """
        Allows access only to not authenticated users.
    """

    message = 'permission denied, at first you must logout'

    def has_permission(self, request, view):
        return bool(request.user.is_anonymous)
