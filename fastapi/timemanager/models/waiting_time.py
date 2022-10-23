from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModelMixin


class WaitingTime(BaseModelMixin):
    exhibit = models.ForeignKey(
        "Exhibit",
        on_delete=models.CASCADE,
        related_name="waiting_times",
    )

    # type = models... # FIXME: implement this
    minutes = models.IntegerField(_("minutes"))
