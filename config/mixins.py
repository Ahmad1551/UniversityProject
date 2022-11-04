from django.db import models
from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from config.settings import LOGIN_URL


class TimeStampedModel(models.Model):
    """Mixin to track model time stamp"""

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class PermissionRequiredMixin(object):
    """Mixin to check if user is in required group"""

    permission_required = ''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('%s?next=%s' % (LOGIN_URL, request.path))
        elif not request.user.is_superuser or not request.user.is_staff or not request.user.has_perm(self.permission_required):
            raise PermissionDenied
        return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)
