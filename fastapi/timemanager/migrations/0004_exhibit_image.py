# Generated by Django 4.1.2 on 2022-10-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timemanager", "0003_waitingtime_type_alter_place_exhibit_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="exhibit",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="exhibits", verbose_name="image"
            ),
        ),
    ]
