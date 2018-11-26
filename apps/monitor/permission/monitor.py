# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework.permissions import BasePermission

__all__ = [
    'MonitorAliyunAPIRequiredMixin', 'MonitorAPIRequiredMixin', 'MonitorVMwareAPIRequiredMixin',
]


class MonitorAPIRequiredMixin(BasePermission):
    def has_permission(self, request, view):
        perms = self.permission_required
        perm_list=list(request.user.get_all_permissions())
        if request.user.is_superuser:
            return True
        if perms in perm_list:
            return True
        else:
            return False


class MonitorAliyunAPIRequiredMixin(MonitorAPIRequiredMixin):
    permission_required = u'monitor.yo_monitor_aliyun'


class MonitorVMwareAPIRequiredMixin(MonitorAPIRequiredMixin):
    permission_required = u'monitor.yo_monitor_vmware'



