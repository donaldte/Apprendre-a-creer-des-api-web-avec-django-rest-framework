from .permissions import IsStaffPermission
from rest_framework import permissions


class StaffEditorPermissionsMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]
