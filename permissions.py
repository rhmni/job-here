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


class IsCompany(BasePermission):
    """
        Allows access only to users that are founder of company.
    """

    message = 'permission denied, you not a founder of company'

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_active and request.user.is_company)


class IsOwnerOfJob(BasePermission):
    """
        Allow access only user that are company and owner of job
    """

    message = 'permission denied, you not owner of this job'

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_active and request.user.is_company)

    def has_object_permission(self, request, view, obj):
        return bool(obj.company == request.user.company)


class IsOwnerOfApplyEmployee(BasePermission):
    """
        Allow access only employee that is owner of apply
    """

    message = 'permission denied, you not owner of this apply'

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_active and not request.user.is_company)

    def has_object_permission(self, request, view, obj):
        return bool(obj.employee == request.user.employee)
