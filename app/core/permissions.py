from rest_framework import permissions
from django.contrib.auth import get_user_model


class SuperuserOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        user = get_object_or_404(get_user_model(), pk=1)
        return user.is_staff
