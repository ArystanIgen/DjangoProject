from rest_framework.permissions import IsAuthenticated
from auth_.models import USER_2,USER_3
from rest_framework.permissions import SAFE_METHODS

class BusinessOrAdminPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user