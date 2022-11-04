from config.models.base import BaseModelMixin
from django.db import models


class Prize(BaseModelMixin):
    MAX_LENGTH_NAME = 50
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    image = models.ImageField(upload_to="prizes", blank=True, null=True)
    count = models.IntegerField(default=0)

    is_first_day = models.BooleanField(default=False, verbose_name="11/5")
    is_second_day = models.BooleanField(default=False, verbose_name="11/6")

    def __str__(self):
        return self.name
