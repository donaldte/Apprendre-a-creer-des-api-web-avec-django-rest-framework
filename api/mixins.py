from .permissions import IsStaffPermission
from rest_framework import permissions


class StaffEditorPermissionsMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]


class UserQuerrySetMixin():
    user_field = 'owner'
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query_data = {} # {'user':'donald'} --> qs.filter(user=donald)
        query_data[self.user_field] = self.request.user
        return qs.filter(**query_data) 
