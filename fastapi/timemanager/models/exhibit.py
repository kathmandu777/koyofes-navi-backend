from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModelMixin


class ExhibitManager(BaseUserManager):
    use_in_migrations = True

    def _create_exhibit(
        self, name: str, password: str | None, **extra_fields
    ) -> "Exhibit":
        if not name:
            raise ValueError("The given name must be set")
        exhibit = self.model(name=name, **extra_fields)
        exhibit.set_password(password)
        exhibit.save(using=self._db)
        return exhibit

    def create_user(
        self, name: str, password: str | None = None, **extra_fields
    ) -> "Exhibit":
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_exhibit(name, password, **extra_fields)

    def create_superuser(
        self, name: str, password: str | None = None, **extra_fields
    ) -> "Exhibit":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_exhibit(name, password, **extra_fields)


class Exhibit(AbstractBaseUser, PermissionsMixin, BaseModelMixin):
    objects = ExhibitManager()

    MIN_LENGTH_USERNAME = 3
    MAX_LENGTH_USERNAME = 20
    name = models.CharField(
        _("name"),
        max_length=MAX_LENGTH_USERNAME,
        unique=True,
    )
    password = models.CharField(_("password"), max_length=1024)

    MAX_LENGTH_DESCRIPTION = 200
    description = models.CharField(
        _("description"), blank=True, max_length=MAX_LENGTH_DESCRIPTION
    )

    # permissions
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    USERNAME_FIELD = "name"

    class Meta:
        verbose_name = _("exhibit")
        verbose_name_plural = _("exhibits")
