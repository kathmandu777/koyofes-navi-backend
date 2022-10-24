from config.models.base import BaseModelMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class WaitingTimeType(models.TextChoices):
    """
    NAME = Value, Label
    """

    IMMEDIATE = "IMMEDIATE", _("待ち時間なし")
    WAITING = "WAITING", _("待ち時間あり")
    RESERVATION = "RESERVATION", _("予約制")


class WaitingTime(BaseModelMixin):
    exhibit = models.ForeignKey(
        "Exhibit",
        on_delete=models.CASCADE,
        related_name="waiting_times",
    )

    type = models.CharField(
        choices=WaitingTimeType.choices,
        max_length=20,
        default=WaitingTimeType.WAITING,
    )
    minutes = models.IntegerField(_("minutes"), default=None, blank=True, null=True)
