from config.models.base import BaseModelMixin
from django.db import models


class Prize(BaseModelMixin):
    MAX_LENGTH_NAME = 50
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    image = models.ImageField(upload_to="prizes", blank=True, null=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
