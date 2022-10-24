from config.models.base import BaseModelMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Place(BaseModelMixin):
    MAX_LENGTH_NAME = 50
    name = models.CharField(_("name"), max_length=MAX_LENGTH_NAME)

    image = models.CharField(_("image"), max_length=1024)
    position_x = models.FloatField(_("position_x"))
    position_y = models.FloatField(_("position_y"))

    exhibit = models.ForeignKey(
        "Exhibit",
        on_delete=models.CASCADE,
    )
