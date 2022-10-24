# Generated by Django 4.1.2 on 2022-10-24 00:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timemanager", "0002_waitingtime_place"),
    ]

    operations = [
        migrations.AddField(
            model_name="waitingtime",
            name="type",
            field=models.CharField(
                choices=[
                    ("IMMEDIATE", "待ち時間なし"),
                    ("WAITING", "待ち時間あり"),
                    ("RESERVATION", "予約制"),
                ],
                default="WAITING",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="exhibit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="waitingtime",
            name="minutes",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="minutes"
            ),
        ),
    ]