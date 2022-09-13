from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import RegisterCerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class AnonPermissionOnly(permissions.BasePermission):
    message = "Login"

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class is_vendor(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            request.user.groups.filter(name='VENDOR').exists()


class IsVendor(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        user = Account.objects.get(user=request.user)
        if not is_authenticated:
            return False

        return user.isVendor
