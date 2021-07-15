from rest_framework.permissions import BasePermission


class IsAnonymoused(BasePermission):
    """
        Allows access only to not authenticated users.
    """

    message = 'permission denied, at first you must logout'

    def has_permission(self, request, view):
        return bool(request.user.is_anonymous)


class IsEmployee(BasePermission):
    """
        Allows access only to users that are employee.
    """

    message = 'permission denied, you not a employee user'

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_active and not request.user.is_company)
