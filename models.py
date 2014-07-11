from django.db import models

import datetime
import functools

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class DateTraceable(models.Model):
    """
    An abstract model mixin that let's you trace the date of creation and
    updating.
    """

    created = models.DateTimeField(
        editable=False,
        verbose_name=_("date created")
    )
    updated = models.DateTimeField(
        editable=False,
        verbose_name=_("date updated")
    )

    class Meta:
        abstract = True

    def trace_date(self):
        now = timezone.now()
        if not self.pk:
            self.created = now
        self.updated = now


class Hideable(models.Model):
    """
    An abstract model mixin that let's you trace the date of creation and
    updating.
    """

    hidden = models.DateTimeField(
        null=True,
        editable=False,
        verbose_name=_("date hidden"),
        db_index=True,
    )

    class Meta:
        abstract = True

    # objects = models.Manager()
    # hidden = VisibilityManager(visible=False)
    # visible = VisibilityManager(visible=True)

    @property
    def is_hidden(self):
        return bool(self.hidden)

    def hide(self):
        now = timezone.now()

