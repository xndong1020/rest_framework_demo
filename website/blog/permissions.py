from rest_framework.permissions import BasePermission


class IsResourceOwnerOrAdminUser(BasePermission):
    message = "You don't have required permission"
    safe_methods = ['GET', 'PUT', 'PATCH', 'DELETE']

    def has_permission(self, request, view):
        if request.method in IsResourceOwnerOrAdminUser.safe_methods:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_superuser
