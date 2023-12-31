# Generated by Django 4.2.3 on 2023-07-31 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("smartsplit", "0004_requests_recipient"),
    ]

    operations = [
        migrations.CreateModel(
            name="SentHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("request_amount", models.FloatField(default=0.0, max_length=100)),
                ("recipient", models.CharField(default="", max_length=100)),
            ],
        ),
    ]
