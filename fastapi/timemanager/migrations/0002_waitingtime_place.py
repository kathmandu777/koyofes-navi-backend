# Generated by Django 4.1.2 on 2022-10-23 13:51

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timemanager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WaitingTime",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="created_at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="updated_at"
                    ),
                ),
                ("minutes", models.IntegerField(verbose_name="minutes")),
                (
                    "exhibit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="waiting_times",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="created_at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="updated_at"
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("image", models.CharField(max_length=1024, verbose_name="image")),
                ("position_x", models.FloatField(verbose_name="position_x")),
                ("position_y", models.FloatField(verbose_name="position_y")),
                (
                    "exhibit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="places",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
