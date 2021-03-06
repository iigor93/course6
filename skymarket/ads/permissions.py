from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "No Permissions"
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "author"):
            return (request.user and request.user.is_authenticated and obj.author == request.user) \
                   or request.user.is_staff or request.user.role == 'admin'
        else:
            return False
